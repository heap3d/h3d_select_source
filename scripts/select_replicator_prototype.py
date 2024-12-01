#!/usr/bin/python
# ================================
# (C)2024 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# select prototype for specified replicator item
# ================================

import modo

from h3d_select_source.scripts.select_item_source import get_replicator_prototypes


def main():
    items: list[modo.Item] = modo.Scene().selected
    sources: set[modo.Item] = set()
    for i in items:
        sources.update(get_replicator_prototypes(i))

    modo.Scene().deselect()
    for i in sources:
        i.select()


if __name__ == '__main__':
    main()
