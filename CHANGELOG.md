# Changelog

## [1.5.1](https://github.com/googleapis/python-notebooks/compare/v1.5.0...v1.5.1) (2023-01-04)


### Documentation

* Minor formatting fixes to reference documentation ([#214](https://github.com/googleapis/python-notebooks/issues/214)) ([17d8096](https://github.com/googleapis/python-notebooks/commit/17d8096ea8691f468829253f2121477481142b36))

## [1.5.0](https://github.com/googleapis/python-notebooks/compare/v1.4.4...v1.5.0) (2022-12-13)


### Features

* Add Instance.reservation_affinity, nic_type, can_ip_forward to v1beta1 API ([05d9b23](https://github.com/googleapis/python-notebooks/commit/05d9b2393136fa296e8def0ec017ca27a8e78497))
* Add IsInstanceUpgradeableResponse.upgrade_image to v1beta1 API ([05d9b23](https://github.com/googleapis/python-notebooks/commit/05d9b2393136fa296e8def0ec017ca27a8e78497))
* Add support for `google.cloud.notebooks.__version__` ([05d9b23](https://github.com/googleapis/python-notebooks/commit/05d9b2393136fa296e8def0ec017ca27a8e78497))
* Add typing to proto.Message based class attributes ([05d9b23](https://github.com/googleapis/python-notebooks/commit/05d9b2393136fa296e8def0ec017ca27a8e78497))
* Add typing to proto.Message based class attributes ([05d9b23](https://github.com/googleapis/python-notebooks/commit/05d9b2393136fa296e8def0ec017ca27a8e78497))
* Added Location and IAM methods ([05d9b23](https://github.com/googleapis/python-notebooks/commit/05d9b2393136fa296e8def0ec017ca27a8e78497))
* Added UpdateRuntime, UpgradeRuntime, DiagnoseRuntime, DiagnoseInstance to v1 API ([05d9b23](https://github.com/googleapis/python-notebooks/commit/05d9b2393136fa296e8def0ec017ca27a8e78497))


### Bug Fixes

* Add dict typing for client_options ([05d9b23](https://github.com/googleapis/python-notebooks/commit/05d9b2393136fa296e8def0ec017ca27a8e78497))
* Deprecate AcceleratorType.NVIDIA_TESLA_K80 ([05d9b23](https://github.com/googleapis/python-notebooks/commit/05d9b2393136fa296e8def0ec017ca27a8e78497))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0 ([05d9b23](https://github.com/googleapis/python-notebooks/commit/05d9b2393136fa296e8def0ec017ca27a8e78497))
* Drop usage of pkg_resources ([05d9b23](https://github.com/googleapis/python-notebooks/commit/05d9b2393136fa296e8def0ec017ca27a8e78497))
* Fix timeout default values ([05d9b23](https://github.com/googleapis/python-notebooks/commit/05d9b2393136fa296e8def0ec017ca27a8e78497))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([05d9b23](https://github.com/googleapis/python-notebooks/commit/05d9b2393136fa296e8def0ec017ca27a8e78497))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([05d9b23](https://github.com/googleapis/python-notebooks/commit/05d9b2393136fa296e8def0ec017ca27a8e78497))

## [1.4.4](https://github.com/googleapis/python-notebooks/compare/v1.4.3...v1.4.4) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#206](https://github.com/googleapis/python-notebooks/issues/206)) ([8e6980a](https://github.com/googleapis/python-notebooks/commit/8e6980afc220c84539da26e9d950a87dc4b75b61))

## [1.4.3](https://github.com/googleapis/python-notebooks/compare/v1.4.2...v1.4.3) (2022-09-29)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#204](https://github.com/googleapis/python-notebooks/issues/204)) ([cd70311](https://github.com/googleapis/python-notebooks/commit/cd703119de83770eccc1cae4c6f5b68ca43fe419))

## [1.4.2](https://github.com/googleapis/python-notebooks/compare/v1.4.1...v1.4.2) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#188](https://github.com/googleapis/python-notebooks/issues/188)) ([f0bd9a2](https://github.com/googleapis/python-notebooks/commit/f0bd9a21ee9c41607f2bb5d0a911e2cb94185169))
* **deps:** require proto-plus >= 1.22.0 ([f0bd9a2](https://github.com/googleapis/python-notebooks/commit/f0bd9a21ee9c41607f2bb5d0a911e2cb94185169))

## [1.4.1](https://github.com/googleapis/python-notebooks/compare/v1.4.0...v1.4.1) (2022-07-13)


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#180](https://github.com/googleapis/python-notebooks/issues/180)) ([f3235d9](https://github.com/googleapis/python-notebooks/commit/f3235d98fae31fb5728594131a74466785ac7cc4))

## [1.4.0](https://github.com/googleapis/python-notebooks/compare/v1.3.2...v1.4.0) (2022-07-07)


### Features

* add audience parameter ([9d37f0d](https://github.com/googleapis/python-notebooks/commit/9d37f0d7563d606d3e7be98e38eb4c98b1e87875))


### Bug Fixes

* **deps:** require google-api-core >= 2.8.0 ([#176](https://github.com/googleapis/python-notebooks/issues/176)) ([9d37f0d](https://github.com/googleapis/python-notebooks/commit/9d37f0d7563d606d3e7be98e38eb4c98b1e87875))
* require python 3.7+ ([#178](https://github.com/googleapis/python-notebooks/issues/178)) ([1dfe877](https://github.com/googleapis/python-notebooks/commit/1dfe8778fc29cb493120165987e2c234b7546e00))

## [1.3.2](https://github.com/googleapis/python-notebooks/compare/v1.3.1...v1.3.2) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#168](https://github.com/googleapis/python-notebooks/issues/168)) ([242d2d1](https://github.com/googleapis/python-notebooks/commit/242d2d162efcbf1c280b0ffc5f510b297de67695))


### Documentation

* fix changelog header to consistent size ([#169](https://github.com/googleapis/python-notebooks/issues/169)) ([a8e4abd](https://github.com/googleapis/python-notebooks/commit/a8e4abda16ad273dd840262d2289c56dc5e9f371))

## [1.3.1](https://github.com/googleapis/python-notebooks/compare/v1.3.0...v1.3.1) (2022-05-05)


### Documentation

* modify the project ID pattern in comment for VmImage ([#162](https://github.com/googleapis/python-notebooks/issues/162)) ([1750ae6](https://github.com/googleapis/python-notebooks/commit/1750ae63d05d58e4bc0801bdc57709151bbac100))

## [1.3.0](https://github.com/googleapis/python-notebooks/compare/v1.2.1...v1.3.0) (2022-04-21)


### Features

* Update Notebooks API for clients libraries ([#154](https://github.com/googleapis/python-notebooks/issues/154)) ([c4a526e](https://github.com/googleapis/python-notebooks/commit/c4a526ed474983b1b18041414a3dc87217ea27aa))

## [1.2.1](https://github.com/googleapis/python-notebooks/compare/v1.2.0...v1.2.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#139](https://github.com/googleapis/python-notebooks/issues/139)) ([8b118ae](https://github.com/googleapis/python-notebooks/commit/8b118ae3d5da2fc3e8edc7b647b1981f4db3dcfb))
* **deps:** require proto-plus>=1.15.0 ([8b118ae](https://github.com/googleapis/python-notebooks/commit/8b118ae3d5da2fc3e8edc7b647b1981f4db3dcfb))

## [1.2.0](https://github.com/googleapis/python-notebooks/compare/v1.1.1...v1.2.0) (2022-02-26)


### Features

* add api key support ([#125](https://github.com/googleapis/python-notebooks/issues/125)) ([72925ba](https://github.com/googleapis/python-notebooks/commit/72925babe34fb97639336e443b2ee588d6727680))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([a0cab1c](https://github.com/googleapis/python-notebooks/commit/a0cab1cbd33f80906dc74bf21d3ca3df62052ef1))


### Documentation

* add generated snippets ([#130](https://github.com/googleapis/python-notebooks/issues/130)) ([dd62813](https://github.com/googleapis/python-notebooks/commit/dd628139a7ec75537342c289d571cacbbba58492))

## [1.1.1](https://www.github.com/googleapis/python-notebooks/compare/v1.1.0...v1.1.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([7750cb3](https://www.github.com/googleapis/python-notebooks/commit/7750cb35928891a955f89ead48c58d5af6b4e2b6))
* **deps:** require google-api-core >= 1.28.0 ([7750cb3](https://www.github.com/googleapis/python-notebooks/commit/7750cb35928891a955f89ead48c58d5af6b4e2b6))


### Documentation

* list oneofs in docstring ([7750cb3](https://www.github.com/googleapis/python-notebooks/commit/7750cb35928891a955f89ead48c58d5af6b4e2b6))

## [1.1.0](https://www.github.com/googleapis/python-notebooks/compare/v1.0.0...v1.1.0) (2021-10-19)


### Features

* add support for python 3.10 ([#102](https://www.github.com/googleapis/python-notebooks/issues/102)) ([40bd0e8](https://www.github.com/googleapis/python-notebooks/commit/40bd0e8ca07a1be91be1246e6f8b142b635365d2))


### Documentation

* fix typos and docstring formatting ([#106](https://www.github.com/googleapis/python-notebooks/issues/106)) ([c094f62](https://www.github.com/googleapis/python-notebooks/commit/c094f62ace6fbf6ffcb205465d262e0a1e68367a))

## [1.0.0](https://www.github.com/googleapis/python-notebooks/compare/v0.4.3...v1.0.0) (2021-10-08)


### Features

* add context manager support in client ([#99](https://www.github.com/googleapis/python-notebooks/issues/99)) ([22efa38](https://www.github.com/googleapis/python-notebooks/commit/22efa38a5e9be1e1137a68329fa947e8a116753c))
* bump release level to production/stable ([#96](https://www.github.com/googleapis/python-notebooks/issues/96)) ([92d6b71](https://www.github.com/googleapis/python-notebooks/commit/92d6b71d5954ca7fab6a4e2a1deaa95c85032e12))

## [0.4.3](https://www.github.com/googleapis/python-notebooks/compare/v0.4.2...v0.4.3) (2021-10-05)


### Documentation

* Fix broken links and formatting in the reference documentation ([#93](https://www.github.com/googleapis/python-notebooks/issues/93)) ([f122cb0](https://www.github.com/googleapis/python-notebooks/commit/f122cb0d638579ebba3b54705f27942660704048))

## [0.4.2](https://www.github.com/googleapis/python-notebooks/compare/v0.4.1...v0.4.2) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([88bbf8f](https://www.github.com/googleapis/python-notebooks/commit/88bbf8f238ad58fa69bf21fa8ecfa48db32b086b))

## [0.4.1](https://www.github.com/googleapis/python-notebooks/compare/v0.4.0...v0.4.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([e1246c8](https://www.github.com/googleapis/python-notebooks/commit/e1246c878c3716181a03dbabee4c5d73e809087f))

## [0.4.0](https://www.github.com/googleapis/python-notebooks/compare/v0.3.2...v0.4.0) (2021-08-31)


### Features

* add Notebooks v1 ([#76](https://www.github.com/googleapis/python-notebooks/issues/76)) ([bc92c07](https://www.github.com/googleapis/python-notebooks/commit/bc92c075369bc93f0b15bd6afa0cc00b8eb9cc77))
* set the default import to notebooks_v1 ([bc92c07](https://www.github.com/googleapis/python-notebooks/commit/bc92c075369bc93f0b15bd6afa0cc00b8eb9cc77))

## [0.3.2](https://www.github.com/googleapis/python-notebooks/compare/v0.3.1...v0.3.2) (2021-07-28)


### Bug Fixes

* enable self signed jwt for grpc ([#68](https://www.github.com/googleapis/python-notebooks/issues/68)) ([ec048cd](https://www.github.com/googleapis/python-notebooks/commit/ec048cd10d04b76fcbac5a246e3bcb6ef81353c8))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#64](https://www.github.com/googleapis/python-notebooks/issues/64)) ([2e9c620](https://www.github.com/googleapis/python-notebooks/commit/2e9c620c45723fe8de13b437fb9642d14b2d8029))


### Miscellaneous Chores

* release as 0.3.2 ([#69](https://www.github.com/googleapis/python-notebooks/issues/69)) ([e3eb4df](https://www.github.com/googleapis/python-notebooks/commit/e3eb4df74a19b88f4f60fab87b9d85349f025ce0))

## [0.3.1](https://www.github.com/googleapis/python-notebooks/compare/v0.3.0...v0.3.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#63](https://www.github.com/googleapis/python-notebooks/issues/63)) ([dcfad3e](https://www.github.com/googleapis/python-notebooks/commit/dcfad3ed534fc8150d0f2ff349da78f22b72b6b3))

## [0.3.0](https://www.github.com/googleapis/python-notebooks/compare/v0.2.0...v0.3.0) (2021-07-01)


### Features

* add always_use_jwt_access ([#56](https://www.github.com/googleapis/python-notebooks/issues/56)) ([a60c86d](https://www.github.com/googleapis/python-notebooks/commit/a60c86d69ebe76897d63ee53b0a7aa44c3a32013))


### Bug Fixes

* disable always_use_jwt_access ([#60](https://www.github.com/googleapis/python-notebooks/issues/60)) ([336ab30](https://www.github.com/googleapis/python-notebooks/commit/336ab303d677415d4c3de172768f8236379c5f90))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-notebooks/issues/1127)) ([#51](https://www.github.com/googleapis/python-notebooks/issues/51)) ([4b4cb00](https://www.github.com/googleapis/python-notebooks/commit/4b4cb00dc4245ab5090eb29434af30a3b4e736a0)), closes [#1126](https://www.github.com/googleapis/python-notebooks/issues/1126)

## [0.2.0](https://www.github.com/googleapis/python-notebooks/compare/v0.1.2...v0.2.0) (2021-05-28)


### Features

* add `from_service_account_info` ([#26](https://www.github.com/googleapis/python-notebooks/issues/26)) ([4999922](https://www.github.com/googleapis/python-notebooks/commit/4999922dc0f6eaebc8aec58929176ab6b87cfdca))
* support self-signed JWT flow for service accounts ([7a84b3b](https://www.github.com/googleapis/python-notebooks/commit/7a84b3b9b8c206a0dc33ccc09821ffa8ee8c3ddd))


### Bug Fixes

* add async client to %name_%version/init.py ([7a84b3b](https://www.github.com/googleapis/python-notebooks/commit/7a84b3b9b8c206a0dc33ccc09821ffa8ee8c3ddd))
* **deps:** add packaging requirement ([#45](https://www.github.com/googleapis/python-notebooks/issues/45)) ([9790dc9](https://www.github.com/googleapis/python-notebooks/commit/9790dc9da532ec396a8d81e3946da53cf243c066))

## [0.1.2](https://www.github.com/googleapis/python-notebooks/compare/v0.1.1...v0.1.2) (2021-02-08)


### Bug Fixes

* remove gRPC send/recv limit ([#12](https://www.github.com/googleapis/python-notebooks/issues/12)) ([8faa7fc](https://www.github.com/googleapis/python-notebooks/commit/8faa7fc87f62590b5c4119dc63d08347ed8eb901))

## [0.1.1](https://www.github.com/googleapis/python-notebooks/compare/v0.1.0...v0.1.1) (2020-08-06)


### Bug Fixes

* fix package name ([#2](https://www.github.com/googleapis/python-notebooks/issues/2)) ([ae80dcf](https://www.github.com/googleapis/python-notebooks/commit/ae80dcffc544a31096e9f076e9538985c1b3a44f))

## 0.1.0 (2020-08-04)


### Features

* generate v1 ([cb8049b](https://www.github.com/googleapis/python-notebooks/commit/cb8049bc35322565c6fd3f04955b756ba9a3415a))
