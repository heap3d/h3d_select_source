#!/usr/bin/python
# ================================
# (C)2024 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# Select replicators where a specified item is used
# ================================

import modo

from scripts.select_items_used import get_replicators


def main():
    selected = modo.Scene().selected

    items_used: list[modo.Item] = []
    for item in selected:
        items_used.extend(get_replicators(item))

    if not items_used:
        return

    modo.Scene().deselect()
    for item in items_used:
        item.select()


if __name__ == '__main__':
    main()
