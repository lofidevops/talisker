#
# Copyright (c) 2015-2021 Canonical, Ltd.
#
# This file is part of Talisker
# (see http://github.com/canonical-ols/talisker).
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

# ignore this whole file for flake8, as when run under py2 it will break
# flake8: noqa

import talisker.util


def test_get_root_exception_implicit():
    exc = None
    try:
        try:
            try:
                raise Exception('root')
            except Exception:
                raise Exception('one')
        except Exception:
            raise Exception('two')
    except Exception as e:
        exc = e

    root = talisker.util.get_root_exception(exc)
    assert root.args == ('root',)


def test_get_root_exception_explicit():
    exc = None
    try:
        try:
            try:
                raise Exception('root')
            except Exception as a:
                raise Exception('one') from a
        except Exception as b:
            raise Exception('two') from b
    except Exception as c:
        exc = c
    root = talisker.util.get_root_exception(exc)
    assert root.args == ('root',)


def test_get_root_exception_mixed():
    exc = None
    try:
        try:
            try:
                raise Exception('root')
            except Exception as a:
                raise Exception('one') from a
        except Exception:
            raise Exception('two')
    except Exception as e:
        exc = e
    root = talisker.util.get_root_exception(exc)
    assert root.args == ('root',)
