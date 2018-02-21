#!/usr/bin/env python3

import os
import sys
import argparse
import logging
import yaml
import shutil, errno
import fileinput

from distutils.version import StrictVersion
from collections import OrderedDict
from copy import deepcopy


class MaxLevelFilter(logging.Filter):

    def __init__(self, level):
        self.level = level


    def filter(self, record):
        return record.levelno < self.level


formatter = logging.Formatter(
    '%(asctime)s [%(threadName)18s][%(module)14s][%(levelname)8s] %(message)s')

# Redirect messages lower than WARNING to stdout
stdout_hdlr = logging.StreamHandler(sys.stdout)
stdout_hdlr.setFormatter(formatter)
log_filter = MaxLevelFilter(logging.WARNING)
stdout_hdlr.addFilter(log_filter)
stdout_hdlr.setLevel(logging.DEBUG)

# Redirect messages higher or equal than WARNING to stderr
stderr_hdlr = logging.StreamHandler(sys.stderr)
stderr_hdlr.setFormatter(formatter)
stderr_hdlr.setLevel(logging.WARNING)

log = logging.getLogger()
log.addHandler(stdout_hdlr)
log.addHandler(stderr_hdlr)

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('version', action='store', type=str, default=os.environ.get('CI_VERSION', None), help='Upcoming version')
    args = parser.parse_args()

    all_versions = _get_all_version()

    if args.version in all_versions:
        log.info(f'version {args.version} already exists')
        sys.exit()

    log.info(f'creating version {args.version}')

    latest_version = _get_latest_version(all_versions)

    new_dir = _copy_folder(latest_version, args.version)
    _update_markdown(new_dir, latest_version, args.version)
    
    _add_left_menu_entry(latest_version, args.version)


def _get_all_version():
    versions=[]

    navigation = yaml.load(open('_data/mps_side_bar.yml', 'r'))
    versions_list = _get_android_verstion_list(navigation)['subsubfolders']
    for version in versions_list:
        # take version after 'Version '
        versions.append(version['title'][len('Version '):])

    return versions


def _get_latest_version(all_versions):
    result = None
    for version in all_versions:
        if result == None:
            result = version
            continue
        
        if StrictVersion(version) > StrictVersion(result):
            result = version
    
    return result


def _copy_folder(old_version, new_version):
    src=f'_docs/Android/Ver.{old_version}'
    dst=f'_docs/Android/Ver.{new_version}'

    log.info(f'copying {src} to {dst}')

    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

    return dst


def _update_markdown(dir, old_version, new_version):
    for root, _, files in os.walk(dir):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                log.info(f'updating file contents in {filepath}')
                with fileinput.input(files=filepath, inplace=True) as f:
                    for line in f:
                        if line.startswith(f'permalink: ver_{old_version}'):
                            line = line.replace(f'permalink: ver_{old_version}', f'permalink: ver_{new_version}')
                        elif file == 'index.md' and line.startswith('title: ') and old_version in line:
                            line = line.replace(old_version, new_version)
                        elif file == 'javadocs.md' and line.startswith('title: ') and old_version in line:
                            line = line.replace(old_version, new_version)
                        elif file == 'javadocs.md' and line.startswith('<a  href') and old_version in line:
                            line = line.replace(old_version, new_version)
                        sys.stdout.write(line)


def _add_left_menu_entry(old_version, new_version):
    log.info(f'adding verson {new_version} to left navigation menu')

    navigation = _ordered_load(open('_data/mps_side_bar.yml', 'r'), yaml.SafeLoader)
    versions_list = _get_android_verstion_list(navigation)['subsubfolders']
    for version_item in versions_list:
        if version_item['title'] == f'Version {old_version}':
            new_version_item = deepcopy(version_item)
            for key, value in new_version_item.items():
                if key == 'title' and value == f'Version {old_version}':
                    new_version_item[key] = f'Version {new_version}'
                elif key == 'subsubfolderitems':
                    for version_sub_item in value:
                        version_sub_item['jurl'] = version_sub_item['jurl'].replace(f'/ver_{old_version}', f'/ver_{new_version}')
                        
            versions_list.insert(0, new_version_item)
            break

    _ordered_dump(navigation, stream=open('_data/mps_side_bar.yml', 'w'), Dumper=yaml.SafeDumper)


def _get_android_verstion_list(nav):
    for folder in nav['folders']:
        if folder['title'] == 'Android':
            for folderitem in folder['folderitems']:
                for subfolder in folderitem.get('subfolders'):
                    if subfolder['title'] == 'Versions':
                        for subfolderitem in subfolder['subfolderitems']:
                            return subfolderitem
    return None


def _ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass
    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)


def _ordered_dump(data, stream=None, Dumper=yaml.Dumper, **kwds):
    class OrderedDumper(Dumper):
        pass
    def _dict_representer(dumper, data):
        return dumper.represent_mapping(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
            data.items())
    OrderedDumper.add_representer(OrderedDict, _dict_representer)
    return yaml.dump(data, stream, OrderedDumper, **kwds)


if __name__ == '__main__':
    main()
