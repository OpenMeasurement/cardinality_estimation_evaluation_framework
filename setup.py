# Copyright 2020 The Private Cardinality Estimation Framework Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Installs wfa_cardinality_estimation_evaluation_framework."""
from setuptools import setup

setup(
    name='wfa_cardinality_estimation_evaluation_framework',
    version='0.0',
    description='Methods for Estimating the Union of Multiple Sets',
    python_requires='>=3.6',
    package_dir={'wfa_cardinality_estimation_evaluation_framework': 'src'},
    packages=[
        'wfa_cardinality_estimation_evaluation_framework',
        'wfa_cardinality_estimation_evaluation_framework.common',
        'wfa_cardinality_estimation_evaluation_framework.estimators',
        'wfa_cardinality_estimation_evaluation_framework.evaluations',
        'wfa_cardinality_estimation_evaluation_framework.evaluations.data',
        'wfa_cardinality_estimation_evaluation_framework.simulations',
    ],
    entry_points={
        'console_scripts': [
            'wfa-run-evaluation=wfa_cardinality_estimation_evaluation_framework'
                                '.evaluations.__main__:main'
        ]
    }
)
