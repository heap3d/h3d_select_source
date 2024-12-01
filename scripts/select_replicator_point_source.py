#!/usr/bin/python
# ================================
# (C)2024 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# select point source for specified repliicator item
# ================================

import modo

from h3d_select_source.scripts.select_item_source import get_replicator_point_source


def main():
    items: list[modo.Item] = modo.Scene().selected
    sources: set[modo.Item] = set()
    for i in items:
        sources.add(get_replicator_point_source(i))

    modo.Scene().deselect()
    for i in sources:
        i.select()


if __name__ == '__main__':
    main()
