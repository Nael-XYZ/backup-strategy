# Backup Strategy 💾

Automated encrypted backups with S3 replication and point-in-time recovery.

## Features

- **Encryption**: AES-256-GCM at rest
- **Compression**: zstd for speed, gzip for compatibility
- **S3 Replication**: Cross-region with versioning
- **Point-in-time**: Hourly snapshots with retention
- **Restore**: One-command full restore

## Schedule

| Data | Frequency | Retention | Storage |
|------|-----------|-----------|---------|
| Database | Hourly | 30 days | 50GB |
| Files | Daily | 90 days | 200GB |
| Config | On change | Forever | 1GB |

## License

MIT