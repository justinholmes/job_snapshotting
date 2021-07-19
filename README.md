Helper class to snapshot the current job stage to GCS for recovery

Example snapshot current stage to GCS

```python
from job_snapshotting.snapshot import Snapshot

snapshot = Snapshot("test", '2018-12-18 14:21:20.021272', 'justin-test-snapshot')
   
snapshot.complete_stage()
print(snapshot.get_current_stage())
    
snapshot.finished_job()
```