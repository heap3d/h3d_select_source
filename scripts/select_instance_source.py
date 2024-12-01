#!/usr/bin/python
# ================================
# (C)2024 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# select source of specified instance item
# ================================

import modo

from h3d_select_source.scripts.select_item_source import get_instance_source


def main():
    items: list[modo.Item] = modo.Scene().selected
    sources: list[modo.Item] = []
    for i in items:
        source_item = get_instance_source(i)
        if source_item:
            sources.append(source_item)

    if not sources:
        return

    modo.Scene().deselect()
    for i in set(sources):
        if i:
            i.select()


if __name__ == '__main__':
    main()
