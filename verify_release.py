"""Verify a downloaded FinNews release without packages, accounts or model requests."""
import argparse,hashlib,json,zipfile
from pathlib import Path

EXPECTED='64d5c17eec084e1c387d76b022a1f19b9416761f0575517da99acea798ecd864'
p=argparse.ArgumentParser();p.add_argument('archive',type=Path);a=p.parse_args()
h=hashlib.sha256(a.archive.read_bytes()).hexdigest()
if h!=EXPECTED:raise SystemExit('Archive SHA256 mismatch')
with zipfile.ZipFile(a.archive) as z:
    names=z.namelist()
    for n in names:
        if '..' in Path(n).parts or Path(n).is_absolute():raise SystemExit('Unsafe archive member')
    events=[json.loads(x) for x in z.read('data/events.jsonl').decode('utf8').splitlines() if x]
    facts=[json.loads(x) for x in z.read('data/evidence.jsonl').decode('utf8').splitlines() if x]
    states=[json.loads(x) for x in z.read('data/real_agent_economic_states.jsonl').decode('utf8').splitlines() if x]
    assert len(events)==156 and len(facts)==1200 and len(states)==36
    assert len({e['asset'] for e in events})==13
print(json.dumps({'archive_sha256':h,'events':len(events),'numeric_facts':len(facts),'real_agent_states':len(states),'network_used':False,'status':'PASS'}))
