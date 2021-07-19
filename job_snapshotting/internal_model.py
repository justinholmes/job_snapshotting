from marshmallow import Schema, fields


class SnapshotSchema(Schema):
    name = fields.Str()
    stage = fields.Integer()


class SnapshotModel(object):
    def __init__(self, name, job_run_timestamp):
        self.name = name
        self.stage = 0
        self.job_run_timestamp = job_run_timestamp
