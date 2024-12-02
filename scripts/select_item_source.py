#!/usr/bin/python
# ================================
# (C)2024 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# select item source
# ================================

from typing import Iterable, Union

import modo

from h3d_utilites.scripts.h3d_debug import h3dd


def main():
    selected = modo.Scene().selected

    source_items: list[modo.Item] = []
    for item in selected:
        source = get_instance_source(item)
        if source:
            source_items.append(source)
        sources = get_replicator_prototypes(item)
        source_items.extend(sources)

    if not source_items:
        return

    modo.Scene().deselect()
    for item in source_items:
        item.select()


def get_instance_source(instance: modo.Item) -> Union[None, modo.Item]:
    try:
        return instance.itemGraph('source').forward()[0]
    except IndexError:
        return None


def get_replicator_prototypes(replicator: modo.Item) -> Iterable[modo.Item]:
    prototypes = [
        i
        for i in replicator.itemGraph('particle').forward()
        if (i.type != 'replicator' or replicator.type == 'replicator')
    ]

    return prototypes


def get_replicator_point_source(replicator: modo.Item) -> Union[None, modo.Item]:
    try:
        source_item = replicator.itemGraph('particle').reverse()[0]
        if (source_item.type == 'replicator' and replicator.type != 'replicator'):
            return None

        return source_item

    except IndexError:
        return None


if __name__ == '__main__':
    h3dd.enable_debug_output(False)
    main()
