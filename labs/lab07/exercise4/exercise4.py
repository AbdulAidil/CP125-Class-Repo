def apply_upgrade(current, upgrade):
    new_permissions = current.copy()
    for perm, level in upgrade.items():
        if perm not in current or level > current[perm]:
            new_permissions[perm] = level
    return new_permissions



current = {"read": 2, "write": 1, "admin": 0}
upgrade = {"read": 1, "write": 3, "execute": 2}
result = apply_upgrade(current, upgrade)
print(result)
print(current)   # Should be unchanged
