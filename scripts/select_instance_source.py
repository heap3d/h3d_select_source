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
    sources: list[modo.Item] = [get_instance_source(i) for i in items]

    modo.Scene().deselect()
    for i in set(sources):
        i.select()


if __name__ == '__main__':
    main()
