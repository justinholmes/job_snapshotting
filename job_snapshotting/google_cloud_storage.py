import json
import os

from google.cloud import storage

from job_snapshotting.internal_model import SnapshotModel


class GoogleCloudStorage:
    _client = storage.Client(project=os.environ.get('project', 'default'))

    def __init__(self, bucket_id, snapshot_schema):
        self._bucket = self._client.get_bucket(bucket_id)
        self._snapshot_schema = snapshot_schema

    def save(self, snapshot_model):
        blob = self._get_blob(snapshot_model.job_run_timestamp, snapshot_model.name)
        blob.upload_from_string(str(self._snapshot_schema.dumps(snapshot_model)), content_type='application/json')

    def load(self, name, job_run_timestamp):
        blob = self._get_blob(job_run_timestamp, name)
        if blob.exists():
            decode = blob.download_as_string().decode("utf-8")
            decode = json.loads(decode)
            snapshot_model = SnapshotModel(decode['name'], job_run_timestamp)
            snapshot_model.stage = decode['stage']
            return snapshot_model
        else:
            model = SnapshotModel(name, job_run_timestamp)
            self.save(model)
            return model

    def _get_blob(self, job_run_timestamp, name):
        blob = self._bucket.blob("{}-{}".format(name, job_run_timestamp))
        return blob

    def delete(self, snapshot_model):
        blob = self._get_blob(snapshot_model.job_run_timestamp, snapshot_model.name)
        if blob.exists():
            blob.delete()
