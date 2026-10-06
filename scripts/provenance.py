"""Freeze the local engine and schemas; this is a code receipt, not a model log."""
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform
import sys

import workspace


def assert_execution(root):
    """Refuse mutation with an installed engine that differs from the frozen version."""
    manifest_path=workspace.contained_path(root,'engine-manifest.json')
    if not manifest_path.is_file(): return  # Existing structured projects without a snapshot.
    manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
    base=Path(__file__).resolve().parent.parent
    for record in manifest['files']:
        relative=record['path'].removeprefix('runtime-snapshot/')
        source=base/relative
        if not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest()!=record['sha256']:
            raise workspace.WorkspaceError('当前执行代码与冻结版本不一致；使用项目 runtime-snapshot/scripts 继续: '+relative)


def capture(root):
    base=Path(__file__).resolve().parent.parent
    manifest_path=workspace.contained_path(root,'engine-manifest.json')
    if manifest_path.exists():
        manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
        for record in manifest['files']:
            target=workspace.contained_path(root,record['path'])
            if hashlib.sha256(target.read_bytes()).hexdigest()!=record['sha256']:
                raise workspace.WorkspaceError('冻结运行代码已改变: '+record['path'])
        return manifest
    files=[]
    candidates=[p for p in sorted((base/'scripts').glob('*.py')) if not p.name.startswith('test_')]
    candidates+=sorted((base/'schemas').glob('*.schema.json'))
    for source in candidates:
        relative='runtime-snapshot/'+source.relative_to(base).as_posix()
        target=workspace.contained_path(root,relative)
        target.parent.mkdir(parents=True,exist_ok=True)
        data=source.read_bytes()
        if target.exists() and target.read_bytes()!=data:
            raise workspace.WorkspaceError('拒绝覆盖不同运行代码: '+relative)
        if not target.exists(): target.write_bytes(data)
        files.append({'path':relative,'sha256':hashlib.sha256(data).hexdigest()})
    packages={}
    for name in ('jsonschema','numpy','pandas','scipy','statsmodels'):
        try: packages[name]=importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError: packages[name]=None
    manifest={'schema_version':1,'id':'engine-manifest','contract_version':1,
              'runtime':{'python':sys.version.split()[0],'system':platform.system(),'machine':platform.machine(),'packages':packages},
              'files':files,'model_identity':'current Codex session; exact model ID and token usage unavailable',
              'meaning':'Frozen code and schemas, not a transcript or a claim of semantic correctness'}
    manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return manifest
