#!/bin/bash

# Batch operations examples
# 批量操作示例

# Configure multiple similar directories
echo "=== Batch Configuration ==="
for dir in data config logs temp; do
    permissionctl register ~/project/$dir project --mode 0750
done

# Configure multiple log files
for logfile in access error debug; do
    permissionctl register /var/log/myapp/$logfile logs --mode 0640 --attributes "+a"
done

# Apply configurations
permissionctl apply project
permissionctl apply logs

# Clean up old configurations
echo "=== Cleanup Old Configurations ==="
for dsl in old_config backup_rules temp_settings; do
    permissionctl delete $dsl
done 