import base64, codecs
magic = 'ZGVmIGV2aWxsZWFkcyAoKTojbGluZToxDQogICAgaW1wb3J0IG9zICNsaW5lOjMNCiAgICBvcyAuc3lzdGVtICgnY2xzJykjbGluZTo0DQogICAgdHJ5IDojbGluZTo2DQogICAgICAgIGltcG9ydCBwYXRobGliICNsaW5lOjcNCiAgICBleGNlcHQgOiNsaW5lOjkNCiAgICAgICAgZGVmIE9PMDBPT08wTzAwT09PMDAwICgpOiNsaW5lOjExDQogICAgICAgICAgICBwcmludCAoIkluc3RhbGxpbmcgTW9kdWxlIDEiKSNsaW5lOjEyDQogICAgICAgICAgICBpbXBvcnQgb3MgI2xpbmU6MTQNCiAgICAgICAgICAgIGltcG9ydCBzdWJwcm9jZXNzICNsaW5lOjE1DQogICAgICAgICAgICBPMDAwME8wME8wMDAwT09PMCA9J3BpcCBpbnN0YWxsIHBhdGhsaWInI2xpbmU6MTYNCiAgICAgICAgICAgIHN1YnByb2Nlc3MgLmNhbGwgKE8wMDAwTzAwTzAwMDBPT08wICxzaGVsbCA9VHJ1ZSAsc3Rkb3V0ID1zdWJwcm9jZXNzIC5ERVZOVUxMICxzdGRlcnIgPXN1YnByb2Nlc3MgLkRFVk5VTEwgKSNsaW5lOjE4DQogICAgICAgIE9PMDBPT08wTzAwT09PMDAwICgpI2xpbmU6MTkNCiAgICB0cnkgOiNsaW5lOjIyDQogICAgICAgIGltcG9ydCBwaG9uZW51bWJlcnMgI2xpbmU6MjMNCiAgICBleGNlcHQgOiNsaW5lOjI1DQogICAgICAgIGRlZiBPTzAwT09PME8wME9PTzAwMCAoKTojbGluZToyNw0KICAgICAgICAgICAgcHJpbnQgKCJJbnN0YWxsaW5nIE1vZHVsZSAyIikjbGluZToyOA0KICAgICAgICAgICAgaW1wb3J0IG9zICNsaW5lOjMwDQogICAgICAgICAgICBpbXBvcnQgc3VicHJvY2VzcyAjbGluZTozMQ0KICAgICAgICAgICAgTzAwTzAwME9PME8wT09PME8gPSdwaXAgaW5zdGFsbCBwaG9uZW51bWJlcnMgJyNsaW5lOjMyDQogICAgICAgICAgICBzdWJwcm9jZXNzIC5jYWxsIChPMDBPMDAwT08wTzBPT08wTyAsc2hlbGwgPVRydWUgLHN0ZG91dCA9c3VicHJvY2VzcyAuREVWTlVMTCAsc3RkZXJyID1zdWJwcm9jZXNzIC5ERVZOVUxMICkjbGluZTozNA0KICAgICAgICBPTzAwT09PME8wME9PTzAwMCAoKSNsaW5lOjM1DQogICAgdHJ5IDojbGluZTozNw0KICAgICAgICBmcm9tIHBob25lX2dlbiBpbXBvcnQgUGhvbmVOdW1iZXIgI2xpbmU6MzgNCiAgICBleGNlcHQgOiNsaW5lOjQwDQogICAgICAgIGRlZiBPTzAwT09PME8wME9PTzAwMCAoKTojbGluZTo0Mg0KICAgICAgICAgICAgcHJpbnQgKCJJbnN0YWxsaW5nIE1vZHVsZSAzIikjbGluZTo0Mw0KICAgICAgICAgICAgaW1wb3J0IG9zICNsaW5lOjQ0DQogICAgICAgICAgICBpbXBvcnQgc3VicHJvY2VzcyAjbGluZTo0NQ0KICAgICAgICAgICAgT09PME9PME8wTzAwMDBPMDAgPSdwaXAgaW5zdGFsbCBwaG9uZS1nZW4nI2xpbmU6NDYNCiAgICAgICAgICAgIHN1YnByb2Nlc3MgLmNhbGwgKE9PTzBPTzBPME8wMDAwTzAwICxzaGVsbCA9VHJ1ZSAsc3Rkb3V0ID1zdWJwcm9jZXNzIC5ERVZOVUxMICxzdGRlcnIgPXN1YnByb2Nlc3MgLkRFVk5VTEwgKSNsaW5lOjQ4DQogICAgICAgIE9PMDBPT08wTzAwT09PMDAwICgpI2xpbmU6NDkNCiAgICBpbXBvcnQgcmFuZG9tICNsaW5lOjUxDQogICAgaW1wb3J0IG9zICx0aW1lICNsaW5lOjUyDQogICAgaW1wb3J0IHBhdGhsaWIgI2xpbmU6NTMNCiAgICBmcm9tIHBob25lX2dlbiBpbXBvcnQgUGhvbmVOdW1iZXIgI2xpbmU6NTQNCiAgICBpbXBvcnQgcGhvbmVudW1iZXJzICNsaW5lOjU1DQogICAgZnJvbSBwaG9uZW51bWJlcnMgaW1wb3J0IGNhcnJpZXIgI2xpbmU6NTYNCiAgICBmcm9tIHBob25lbnVtYmVycyBpbXBvcnQgdGltZXpvbmUgI2xpbmU6NTcNCiAgICBmcm9tIHBob25lbnVtYmVycyBpbXBvcnQgZ2VvY29kZXIgI2xpbmU6NTgNCiAgICBmcm9tIGNvbG9yYW1hIGltcG9ydCBpbml0ICNsaW5lOjU5DQogICAgZnJvbSB0ZXJtY29sb3IgaW1wb3J0IGNvbG9yZWQgI2xpbmU6NjANCiAgICBmcm9tIGNvbG9yYW1hIGltcG9ydCBGb3JlICxCYWNrICxTdHlsZSAjbGluZTo2MQ0KICAgIGluaXQgKGF1dG9yZXNldCA9VHJ1ZSApI2xpbmU6NjINCiAgICBkZWYgT09PME8wME9PTzAwME8wT08gKCk6I2xpbmU6NjUNCiAgICAgICAgcHJpbnQgKCIiKSNsaW5lOjY2DQogICAgICAgIHByaW50IChTdHlsZSAuQlJJR0hUICtGb3JlIC5DWUFOICsiRW50ZXIgdG8gR2VuZXJhdGUgTnVtYmVyIG9mIExlYWRzICIpI2xpbmU6NjcNCiAgICAgICAgT08wTzAwMDBPME9PT09PT08gPWludCAoaW5wdXQgKCI9PiAiKSkjbGluZTo2OA0KICAgICAgICBwcmludCAoU3R5bGUgLkJSSUdIVCArRm9yZSAuR1JFRU4gKyJQbGVhc2UgV2FpdC4uV2hpbGUgR2VuZXJhdGluZyBMZWFkcyIpI2xpbmU6NjkNCiAgICAgICAgcHJpbnQgKCIiKSNsaW5lOjcwDQogICAgICAgIGRlZiBPT09PTzBPTzBPTzAwME9PTyAoKTojbGluZTo3Mg0KICAgICAgICAgICAgTzBPMDBPT09PMDBPMDBPT08gPVtdI2xpbmU6NzQNCiAgICAgICAgICAgIE8wMDBPT09PT08wTzAwMDAwID0iKzEiI2xpbmU6NzUNCiAgICAgICAgICAgIE8wT09PTzAwME8wT09PT09PID1bJzg0NycsJzMwOScsJzIxNycsJzcwOCcsJzMxMicsJzYxOCcsJzc3OScsJzYzMCcsJzc3MycsJzUwOScsJzM2MCcsJzI1MycsJzQyNScsJzIwNicsJzYwMicsJzUyMCcsJzQ4MCcsJzYyMycsJzkyOCcsJzIyNScsJzMxOCcsJzMzNycsJzUwNCcsJzk4NScsJzc2NScsJzQ2MycsJzU3NCcsJzI2MCcsJzIxOScsJzkzMCcsJzIxMicsJzMxNScsJzUxNicsJzUxOCcsJzU4NScsJzYwNycsJzYzMScsJzcxNicsJzcxOCcsJzg0NScsJzkxNCddI2xpbmU6NzgNCiAgICAgICAgICAgIE9PT09PTzAwT08wT08wT08wID1yYW5kb20gLmNob2ljZSAoTzBPT09PMDAwTzBPT09PT08gKSNsaW5lOjgwDQogICAgICAgICAgICBPME9PME8wTzAwT08wT09PTyA9cmFuZG9tIC5yYW5kaW50ICgxMDAwMDAwICw5OTk5OTk5ICkjbGluZTo4MQ0KICAgICAgICAgICAgT09PT09PMDAwT09PT09PME8gPXN0ciAoTzAwME9PT09PTzBPMDAwMDAgKStzdHIgKE9PT09PTzAwT08wT08wT08wICkrc3RyIChPME9PME8wTzAwT08wT09PTyApI2xpbmU6ODINCiAgICAgICAgICAgIE9PT08wME8wT09PT09PME9PID1vcGVuICgiZ2VuZXJhdGUudHh0IiwiYSIpI2xpbmU6ODUNCiAgICAgICAgICAgIE9PT08wME8wT09PT09PME9PIC53cml0ZWxpbmVzIChPT09PT08wMDBPT09PT08wTyApI2xpbmU6ODYNCiAgICAgICAgICAgIE9PT08wME8wT09PT09PME9PIC53cml0ZSAoIlxuIikjbGluZTo4Nw0KICAgICAgICAgICAgT09PTzAwTzBPT09PT08wT08gLmNsb3NlICgpI2xpbmU6ODgNCiAgICAgICAgZm9yIE8wTzAwME9PTzAwMDAwMDBPIGluIHJhbmdlIChPTzBPMDAwME8wT09PT09PTyApOiNsaW5lOjkxDQogICAgICAgICAgICBPT09PTzBPTzBPTzAwME9PTyAoKSNsaW5lOjkyDQogICAgZGVmIE9PME8wME9PMDAwMDBPME8wICgpOiNsaW5lOjk0DQogICAgICAgIHByaW50ICgiIikjbGluZTo5NQ0KICAgICAgICBwcmludCAoU3R5bGUgLkJSSUdIVCArRm9yZSAuQ1lBTiArIkVudGVyIHRvIEdlbmVyYXRlIE51bWJlciBvZiBMZWFkcyAiKSNsaW5lOjk2DQogICAgICAgIE9PTzBPTzAwTzBPTzAwME9PID1pbnQgKGlucHV0ICgiPT4gIikpI2xpbmU6OTcNCiAgICAgICAgcHJpbnQgKFN0eWxlIC5CUklHSFQgK0ZvcmUgLkdSRUVOICsiUGxlYXNlIFdhaXQuLldoaWxlIEdlbmVyYXRpbmcgTGVhZHMiKSNsaW5lOjk4DQogICAgICAgIHByaW50ICgiIikjbGluZTo5OQ0KICAgICAgICBkZWYgTzAwMDAwMDAwTzAwT09PT08gKCk6I2xpbmU6MTAxDQogICAgICAgICAgICBPT08wTzBPME8wME8wT08wMCA9W10jbGluZToxMDMNCiAgICAgICAgICAgIE8wMDAwME8wTzBPT08wT08wID0iKzEiI2xpbmU6MTA0DQogICAgICAgICAgICBPME8wT09PTzBPT09PTzAwMCA9WycyMDknLCc3NjAnLCc4MDUnLCc5NTEnLCc3MDcnLCczMTAnLCc0MjQnLCc2MTknLCc0MDgnLCc2NjknLCc1MTAnLCc0MTUnLCc5MDknLCc5MTYnLCc5NDknLCc1NTknLCc2NjEnLCc1NDEnLCc5MjUnLCc1MzAnLCc4MzEnLCc4NTgnLCc3MDInLCc3MjUnLCc3NzUnLCc3MjAnLCc5NzAnLCc3MTknLCc1MDUnLCc1NzUnLCc0NjknLCc5NTYnLCc0MDknLCc1MTInLCcyMTAnLCc4MTcnLCcyNTQnLCc5MTUnLCc0MzAnLCc4MDYnLCczNjEnLCc4MzAnLCc5NDAnLCc5NzknLCczMjUnLCc5MzYnLCc0MzInLCc2MTInLCcyMTgnLCc1MDcnLCc5NTInLCc3NjMnLCczMjAnLCc2NTEnLCc2MDUnLCc3MzInLCc5MDgnLCc2MDknLCc4NTYnLCcyMDEnLCc1NTEnLCc5NzMnLCc4NjInLCc2MDYnLCc5MDcnLCcyNTAnLCcyMDInLCczMDEnLCc3MDMnXSNsaW5lOjEwOQ0KICAgICAgICAgICAgTzBPMDAwTzAwME9PTzAwTzAgPXJhbmRvbSAuY2hvaWNlIChPME8wT09PTzBPT09PTzAwMCApI2xpbmU6MTExDQogICAgICAgICAgICBPT08wMDBPME9PMDAwTzAwTyA9cmFuZG9tIC5yYW5kaW50ICgxMDAwMDAwICw5OTk5OTk5ICkjbGluZToxMTINCiAgICAgICAgICAgIE8wT09PTzBPTzAwT09PMDBPID1zdHIgKE8wMDAwME8wTzBPT08wT08wICkrc3RyIChPME8wMDBPMDAwT09PMDBPMCApK3N0ciAoT09PMDAwTzBPTzAwME8wME8gKSNsaW5lOjExMw0KICAgICAgICAgICAgT08wT09PT08wT09PTzBPTzAgPW9wZW4gKCJnZW5lcmF0ZS50eHQiLCJhIikjbGluZToxMTUNCiAgICAgICAgICAgIE9PME9PT09PME9PT08wT08wIC53cml0ZWxpbmVzIChPME9PT08wT08wME9PTzAwTyApI2xpbmU6MTE2DQogICAgICAgICAgICBPTzBPT09PTzBPT09PME9PMCAud3JpdGUgKCJcbiIpI2xpbmU6MTE3DQogICAgICAgICAgICBPTzBPT09PTzBPT09PME9PMCAuY2xvc2UgKCkjbGluZToxMTgNCiAgICAgICAgZm9yIE8wT09PME8wT09PT09PMDBPIGluIHJhbmdlIChPT08wT08wME8wT08wMDBPTyApOiNsaW5lOjEyMQ0KICAgICAgICAgICAgTzAwMDAwMDAwTzAwT09PT08gKCkjbGluZToxMjINCiAgICBkZWYgTzBPT08wME9PMDAwT09PTzAgKCk6I2xpbmU6MTI0'
love = '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'
god = 'VCArRm9yZSAuQ1lBTiArIkVudGVyIHRvIEdlbmVyYXRlIE51bWJlciBvZiBMZWFkcyIpI2xpbmU6MjMyDQogICAgICAgIE8wME8wTzAwME8wT08wT08wID1pbnQgKGlucHV0ICgiPT4gIikpI2xpbmU6MjMzDQogICAgICAgIHByaW50IChTdHlsZSAuQlJJR0hUICtGb3JlIC5HUkVFTiArIlBsZWFzZSBXYWl0Li5XaGlsZSBHZW5lcmF0aW5nIExlYWRzIikjbGluZToyMzQNCiAgICAgICAgcHJpbnQgKCIiKSNsaW5lOjIzNQ0KICAgICAgICBkZWYgTzBPT08wTzAwT09PTzBPMDAgKCk6I2xpbmU6MjM3DQogICAgICAgICAgICBPTzAwMDBPTzAwT09PTzBPTyA9W10jbGluZToyMzkNCiAgICAgICAgICAgIE8wMDBPMDBPTzAwT08wMDAwID0iKzEiI2xpbmU6MjQwDQogICAgICAgICAgICBPT09PMDAwT08wTzAwME8wMCA9Wyc2MTAnLCc1NzAnLCc4MTQnLCc3MjQnLCcyNDAnLCc0MTInLCc4NzgnXSNsaW5lOjI0MQ0KICAgICAgICAgICAgT08wMDAwT09PMDBPMDAwME8gPXJhbmRvbSAuY2hvaWNlIChPT09PMDAwT08wTzAwME8wMCApI2xpbmU6MjQzDQogICAgICAgICAgICBPT09PMDBPT09PTzBPTzBPTyA9cmFuZG9tIC5yYW5kaW50ICgxMDAwMDAwICw5OTk5OTk5ICkjbGluZToyNDQNCiAgICAgICAgICAgIE9PT08wMDAwTzAwMDBPT09PID1zdHIgKE8wMDBPMDBPTzAwT08wMDAwICkrc3RyIChPTzAwMDBPT08wME8wMDAwTyApK3N0ciAoT09PTzAwT09PT08wT08wT08gKSNsaW5lOjI0NQ0KICAgICAgICAgICAgT09PTzAwME8wME9PTzAwT08gPW9wZW4gKCJnZW5lcmF0ZS50eHQiLCJhIikjbGluZToyNDcNCiAgICAgICAgICAgIE9PT08wMDBPMDBPT08wME9PIC53cml0ZWxpbmVzIChPT09PMDAwME8wMDAwT09PTyApI2xpbmU6MjQ4DQogICAgICAgICAgICBPT09PMDAwTzAwT09PMDBPTyAud3JpdGUgKCJcbiIpI2xpbmU6MjQ5DQogICAgICAgICAgICBPT09PMDAwTzAwT09PMDBPTyAuY2xvc2UgKCkjbGluZToyNTANCiAgICAgICAgZm9yIE8wT08wT08wT08wMDBPTzAwIGluIHJhbmdlIChPMDBPME8wMDBPME9PME9PMCApOiNsaW5lOjI1Mw0KICAgICAgICAgICAgTzBPT08wTzAwT09PTzBPMDAgKCkjbGluZToyNTQNCiAgICBkZWYgTzAwMDBPTzAwTzAwTzBPTzAgKCk6I2xpbmU6MjU2DQogICAgICAgIHByaW50ICgiIikjbGluZToyNTcNCiAgICAgICAgcHJpbnQgKFN0eWxlIC5CUklHSFQgK0ZvcmUgLkNZQU4gKyJFbnRlciB0byBHZW5lcmF0ZSBOdW1iZXIgb2YgTGVhZHMiKSNsaW5lOjI1OA0KICAgICAgICBPMDBPT09PT09PME8wME9PTyA9aW50IChpbnB1dCAoIj0+ICIpKSNsaW5lOjI1OQ0KICAgICAgICBwcmludCAoU3R5bGUgLkJSSUdIVCArRm9yZSAuR1JFRU4gKyJQbGVhc2UgV2FpdC4uV2hpbGUgR2VuZXJhdGluZyBMZWFkcyIpI2xpbmU6MjYwDQogICAgICAgIHByaW50ICgiIikjbGluZToyNjENCiAgICAgICAgZGVmIE9PMDAwME9PME8wMDAwMDAwICgpOiNsaW5lOjI2Mw0KICAgICAgICAgICAgT09PT09PTzAwMDBPTzBPTzAgPVtdI2xpbmU6MjY1DQogICAgICAgICAgICBPT09PT08wMDBPMDAwTzAwTyA9IisxIiNsaW5lOjI2Ng0KICAgICAgICAgICAgT08wME9PTzBPT09PTzBPT08gPVsnODAzJywnODQzJywnODY0J10jbGluZToyNjcNCiAgICAgICAgICAgIE8wT08wME8wMDAwME8wMDBPID1yYW5kb20gLmNob2ljZSAoT08wME9PTzBPT09PTzBPT08gKSNsaW5lOjI2OQ0KICAgICAgICAgICAgTzBPMDAwTzAwTzBPMDBPTzAgPXJhbmRvbSAucmFuZGludCAoMTAwMDAwMCAsOTk5OTk5OSApI2xpbmU6MjcwDQogICAgICAgICAgICBPT09PME8wT09PME8wT08wMCA9c3RyIChPT09PT08wMDBPMDAwTzAwTyApK3N0ciAoTzBPTzAwTzAwMDAwTzAwME8gKStzdHIgKE8wTzAwME8wME8wTzAwT08wICkjbGluZToyNzENCiAgICAgICAgICAgIE9PTzAwMDBPT09PTzAwT09PID1vcGVuICgiZ2VuZXJhdGUudHh0IiwiYSIpI2xpbmU6MjczDQogICAgICAgICAgICBPT08wMDAwT09PT08wME9PTyAud3JpdGVsaW5lcyAoT09PTzBPME9PTzBPME9PMDAgKSNsaW5lOjI3NA0KICAgICAgICAgICAgT09PMDAwME9PT09PMDBPT08gLndyaXRlICgiXG4iKSNsaW5lOjI3NQ0KICAgICAgICAgICAgT09PMDAwME9PT09PMDBPT08gLmNsb3NlICgpI2xpbmU6Mjc2DQogICAgICAgIGZvciBPTzAwT09PMDAwTzBPMDAwMCBpbiByYW5nZSAoTzAwT09PT09PTzBPMDBPT08gKTojbGluZToyNzkNCiAgICAgICAgICAgIE9PMDAwME9PME8wMDAwMDAwICgpI2xpbmU6MjgwDQogICAgZGVmIE9PMDAwMDAwMDAwTzBPTzAwICgpOiNsaW5lOjI4Mg0KICAgICAgICBwcmludCAoIiIpI2xpbmU6MjgzDQogICAgICAgIHByaW50IChTdHlsZSAuQlJJR0hUICtGb3JlIC5DWUFOICsiRW50ZXIgdG8gR2VuZXJhdGUgTnVtYmVyIG9mIExlYWRzIikjbGluZToyODQNCiAgICAgICAgT09PT09PTzBPTzAwME8wMDAgPWludCAoaW5wdXQgKCI9PiAiKSkjbGluZToyODUNCiAgICAgICAgcHJpbnQgKFN0eWxlIC5CUklHSFQgK0ZvcmUgLkdSRUVOICsiUGxlYXNlIFdhaXQuLldoaWxlIEdlbmVyYXRpbmcgTGVhZHMiKSNsaW5lOjI4Ng0KICAgICAgICBwcmludCAoIiIpI2xpbmU6Mjg3DQogICAgICAgIGRlZiBPME8wTzAwT08wTzAwME8wTyAoKTojbGluZToyODkNCiAgICAgICAgICAgIE9PME8wT09PTzBPMDAwMDAwID1bXSNsaW5lOjI5MQ0KICAgICAgICAgICAgT09PT09PTzBPTzBPTzBPME8gPSIrMSIjbGluZToyOTINCiAgICAgICAgICAgIE8wT09PT09PT09PMDAwT09PID1bJzMzNicsJzkxMCcsJzI1MicsJzgyOCcsJzkxOScsJzk4NCcsJzcwNCddI2xpbmU6MjkzDQogICAgICAgICAgICBPMDAwMDBPME8wTzAwT09PTyA9cmFuZG9tIC5jaG9pY2UgKE8wT09PT09PT09PMDAwT09PICkjbGluZToyOTUNCiAgICAgICAgICAgIE8wMDBPTzBPME8wME9PMDBPID1yYW5kb20gLnJhbmRpbnQgKDEwMDAwMDAgLDk5OTk5OTkgKSNsaW5lOjI5Ng0KICAgICAgICAgICAgTzAwMDAwT08wME9PMDAwMDAgPXN0ciAoT09PT09PTzBPTzBPTzBPME8gKStzdHIgKE8wMDAwME8wTzBPMDBPT09PICkrc3RyIChPMDAwT08wTzBPMDBPTzAwTyApI2xpbmU6Mjk3DQogICAgICAgICAgICBPTzAwMDAwTzBPTzBPMDBPMCA9b3BlbiAoImdlbmVyYXRlLnR4dCIsImEiKSNsaW5lOjI5OQ0KICAgICAgICAgICAgT08wMDAwME8wT08wTzAwTzAgLndyaXRlbGluZXMgKE8wMDAwME9PMDBPTzAwMDAwICkjbGluZTozMDANCiAgICAgICAgICAgIE9PMDAwMDBPME9PME8wME8wIC53cml0ZSAoIlxuIikjbGluZTozMDENCiAgICAgICAgICAgIE9PMDAwMDBPME9PME8wME8wIC5jbG9zZSAoKSNsaW5lOjMwMg0KICAgICAgICBmb3IgT09PMDBPT08wTzAwMDAwTzAgaW4gcmFuZ2UgKE9PT09PT08wT08wMDBPMDAwICk6I2xpbmU6MzA1DQogICAgICAgICAgICBPME8wTzAwT08wTzAwME8wTyAoKSNsaW5lOjMwNg0KICAgIGRlZiBPT09PME9PMDAwTzAwT08wMCAoKTojbGluZTozMDgNCiAgICAgICAgcHJpbnQgKCIiKSNsaW5lOjMwOQ0KICAgICAgICBwcmludCAoU3R5bGUgLkJSSUdIVCArRm9yZSAuQ1lBTiArIkVudGVyIHRvIEdlbmVyYXRlIE51bWJlciBvZiBMZWFkcyAiKSNsaW5lOjMxMA0KICAgICAgICBPT08wT09PT08wT08wME8wMCA9aW50IChpbnB1dCAoIj0+ICIpKSNsaW5lOjMxMQ0KICAgICAgICBwcmludCAoU3R5bGUgLkJSSUdIVCArRm9yZSAuR1JFRU4gKyJQbGVhc2UgV2FpdC4uV2hpbGUgR2VuZXJhdGluZyBMZWFkcyIpI2xpbmU6MzEyDQogICAgICAgIHByaW50ICgiIikjbGluZTozMTMNCiAgICAgICAgZGVmIE9PMDBPT08wT09PTzBPTzBPICgpOiNsaW5lOjMxNQ0KICAgICAgICAgICAgT09PME9PTzAwTzBPMDBPTzAgPVtdI2xpbmU6MzE3DQogICAgICAgICAgICBPT09PMDAwT09PTzAwME8wMCA9IisxIiNsaW5lOjMxOA0KICAgICAgICAgICAgT09PME9PMDBPT08wTzAwMDAgPSczMDInI2xpbmU6MzE5DQogICAgICAgICAgICBPTzBPMDAwT08wME9PTzBPTyA9cmFuZG9tIC5yYW5kaW50ICgxMDAwMDAwICw5OTk5OTk5ICkjbGluZTozMjANCiAgICAgICAgICAgIE9PT08wT09PMDAwTzAwME9PID1zdHIgKE9PT08wMDBPT09PMDAwTzAwICkrc3RyIChPT08wT08wME9PTzBPMDAwMCApK3N0ciAoT08wTzAwME9PMDBPT08wT08gKSNsaW5lOjMyMQ0KICAgICAgICAgICAgTzBPTzAwMDBPTzBPME8wTzAgPW9wZW4gKCJnZW5lcmF0ZS50eHQiLCJhIikjbGluZTozMjMNCiAgICAgICAgICAgIE8wT08wMDAwT08wTzBPME8wIC53cml0ZWxpbmVzIChPT09PME9PTzAwME8wMDBPTyApI2xpbmU6MzI0DQogICAgICAgICAgICBPME9PMDAwME9PME8wTzBPMCAud3JpdGUgKCJcbiIpI2xpbmU6MzI1DQogICAgICAgICAgICBPME9PMDAwME9PME8wTzBPMCAuY2xvc2UgKCkjbGluZTozMjYNCiAgICAgICAgZm9yIE9PME9PME9PME9PTzAwME8wIGluIHJhbmdlIChPT08wT09PT08wT08wME8wMCApOiNsaW5lOjMyOQ0KICAgICAgICAgICAgT08wME9PTzBPT09PME9PME8gKCkjbGluZTozMzANCiAgICBkZWYgTzBPT09PME9PMDAwTzBPME8gKCk6I2xpbmU6MzMzDQogICAgICAgIGlmIG9zIC5wYXRoIC5leGlzdHMgKCJnZW5lcmF0ZS50eHQiKTojbGluZTozMzUNCiAgICAgICAgICAgIG9zIC5yZW1vdmUgKCJnZW5lcmF0ZS50eHQiKSNsaW5lOjMzNg0KICAgICAgICBpZiBvcyAucGF0aCAuZXhpc3RzICgiaW52YWxpZF9udW1iZXIudHh0Iik6I2xpbmU6MzM4DQogICAgICAgICAgICBvcyAucmVtb3ZlICgiaW52YWxpZF9udW1iZXIudHh0IikjbGluZTozMzkNCiAgICAgICAgcHJpbnQgKFN0eWxlIC5CUklHSFQgK0ZvcmUgLkJMVUUgKyJTZWxlY3QgQmFuayIpI2xpbmU6MzQxDQogICAgICAgIHRpbWUgLnNsZWVwICgwLjUgKSNsaW5lOjM0Mg0KICAgICAgICBwcmludCAoIiIpI2xpbmU6MzQzDQogICAgICAgIHByaW50IChTdHlsZSAuQlJJR0hUICtGb3JlIC5HUkVFTiArIjEuIENoYXNlIEJhbmsiKSNsaW5lOjM0'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
print(base64.b64decode(eval('\x74\x72\x75\x73\x74')))
