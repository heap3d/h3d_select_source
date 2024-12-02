#!/usr/bin/python
# ================================
# (C)2024 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# select item usage
# ================================

import modo


def main():
    selected = modo.Scene().selected

    used_items: list[modo.Item] = []
    for item in selected:
        used_items.extend(get_instances(item))
        used_items.extend(get_replicators(item))

    if not used_items:
        return

    modo.Scene().deselect()
    for item in used_items:
        item.select()


def get_instances(item: modo.Item) -> list[modo.Item]:
    return item.itemGraph('meshInst').forward()


def get_replicators(item: modo.Item) -> list[modo.Item]:
    used_items: list[modo.Item] = []
    used_items.extend(item.itemGraph('particle').reverse())
    used_items.extend(item.itemGraph('particle').forward())

    return used_items


if __name__ == '__main__':
    main()
