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
    selected = modo.Scene.selected

    source_items = []
    for item in selected:
        source = get_instance_source(item)
        if source:
            source_items.append(source)


def get_instance_source(instance: modo.Item) -> Union[None, modo.Item]:
    try:
        return instance.itemGraph('source').forward()[0]
    except IndexError:
        return None


def get_replicator_prototypes(replicator: modo.Item) -> Iterable[modo.Item]:
    return replicator.itemGraph('particle').forward()


def get_replicator_point_source(replicator: modo.Item) -> Union[None, modo.Item]:
    try:
        return replicator.itemGraph('particle').reverse()[0]
    except IndexError:
        return None


if __name__ == '__main__':
    h3dd.enable_debug_output(False)
    main()
