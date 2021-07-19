from job_snapshotting.google_cloud_storage import GoogleCloudStorage
from job_snapshotting.internal_model import SnapshotSchema


class Snapshot:
    def __init__(self, name, job_run_timestamp, bucket_id):
        self._snapshot_schema = SnapshotSchema()
        self._storage = GoogleCloudStorage(bucket_id, self._snapshot_schema)
        self._snapshot_model = self._storage.load(name, job_run_timestamp)

    def get_schema(self):
        return self._snapshot_schema.dump(self._snapshot_model)

    def complete_stage(self):
        self._snapshot_model.stage = self._snapshot_model.stage + 1
        self._storage.save(self._snapshot_model)

    def get_current_stage(self):
        return self._storage.load(self._snapshot_model.name, self._snapshot_model.job_run_timestamp).stage

    def finished_job(self):
        self._storage.delete(self._snapshot_model)
