
# Title: September 18, 2025 
Link: https://cloud.google.com/release-notes#September_18_2025<br>
# Google Kubernetes Engine

## Changed
原文:
 **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.33.4-gke.1134000 is now the default version for cluster creation in the Extended channel.
- The following versions are now available in the Extended channel:

- 1.28.15-gke.2610000
- 1.28.15-gke.2697000
- 1.29.15-gke.1835000
- 1.29.15-gke.1936000
- 1.30.14-gke.1130000
- 1.31.12-gke.1083000
- 1.32.8-gke.1134000
- 1.33.4-gke.1172000

- The following versions are no longer available in the Extended channel:

- 1.28.15-gke.2564000
- 1.28.15-gke.2630000
- 1.29.15-gke.1773000
- 1.29.15-gke.1851000
- 1.30.14-gke.1059000
- 1.31.12-gke.1060000
- 1.32.8-gke.1026000
- 1.33.4-gke.1036000

- Auto-upgrade targets are now available for the following minor versions:

- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version 1.28.15-gke.2599000 with this release.

- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:

- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version 1.28.15-gke.2599000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version 1.29.15-gke.1820000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version 1.30.14-gke.1108000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version 1.32.8-gke.1108000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version 1.33.4-gke.1134000 with this release.

[1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
- 1.28.15-gke.2610000
- 1.28.15-gke.2697000
- 1.29.15-gke.1835000
- 1.29.15-gke.1936000
- 1.30.14-gke.1130000
- 1.31.12-gke.1083000
- 1.32.8-gke.1134000
- 1.33.4-gke.1172000

[1.28.15-gke.2610000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
[1.28.15-gke.2697000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
[1.29.15-gke.1835000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
[1.29.15-gke.1936000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
[1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
[1.31.12-gke.1083000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
[1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
[1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
- 1.28.15-gke.2564000
- 1.28.15-gke.2630000
- 1.29.15-gke.1773000
- 1.29.15-gke.1851000
- 1.30.14-gke.1059000
- 1.31.12-gke.1060000
- 1.32.8-gke.1026000
- 1.33.4-gke.1036000

- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version 1.28.15-gke.2599000 with this release.

[1.28.15-gke.2599000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version 1.28.15-gke.2599000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version 1.29.15-gke.1820000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version 1.30.14-gke.1108000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version 1.32.8-gke.1108000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version 1.33.4-gke.1134000 with this release.

[1.28.15-gke.2599000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
[1.29.15-gke.1820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
[1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
[1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
[1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)

説明：
Extendedチャネルにおいて、クラスタ作成時のデフォルトバージョンが `1.33.4-gke.1134000` に更新されました。また、複数のGKEバージョンが新たに利用可能になり、同時に一部の古いバージョンが利用不可となりました。自動アップグレードが有効なコントロールプレーンおよびノードは、指定されたターゲットバージョン（例: 1.27から1.28.15へのマイナーバージョンアップグレード、または既存のマイナーバージョンに対するパッチアップグレード）にアップグレードされます。

影響有無：
*   **新規クラスタ**: Extendedチャネルでクラスタを作成する際、デフォルトで `1.33.4-gke.1134000` が選択されます。
*   **既存クラスタ**: Extendedチャネルを利用しているGKEクラスタにおいて、自動アップグレードが有効な場合、記載されたターゲットバージョンにアップグレードが実行されます。特に、1.27から1.28へのマイナーバージョンアップグレードは、アプリケーションの互換性に影響を与える可能性があります。現在利用不可となったバージョンを使用しているクラスタは、将来的なサポート終了や手動アップグレードが必要になる可能性があります。
*   **Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)**: Composer 2はGKEクラスタ上で動作するため、Composerインスタンスの基盤となるGKEクラスタがExtendedチャネルを利用しており、かつ自動アップグレードが有効な場合、リストされたターゲットバージョンにアップグレードされる可能性があります。Composer 2.7.1がこれらのGKEバージョンと互換性があるか、およびアップグレード時の動作保証について、Composerの公式ドキュメントで確認することを推奨します。

対処方法：
1.  **バージョン互換性の確認**: Extendedチャネルを利用しているGKEクラスタで動作するアプリケーションやワークロードが、新しいGKEバージョン（特にマイナーバージョンアップグレード対象の1.28.15など）と互換性があるか事前に検証してください。
2.  **アップグレード計画**: 自動アップグレードのタイミングを確認し、必要に応じてメンテナンス期間を設定するか、メンテナンス除外を設定してアップグレードをコントロールしてください。
3.  **古いバージョンの対応**: 利用不可となったバージョンを現在使用している場合は、サポートされているバージョンへのアップグレードを早期に計画し、実行してください。

用語説明：
*   **Extended channel**: GKEのリリースチャネルの一つで、Regularチャネルよりも長期的なサポートを提供し、安定性を重視します。セキュリティパッチやバグ修正が適用された安定版が提供されます。
*   **Auto-upgrade (自動アップグレード)**: GKEクラスタのコントロールプレーンおよびノードが、Google Cloudによって自動的に新しいバージョンにアップグレードされる機能です。
*   **Maintenance exclusions (メンテナンス除外)**: GKEクラスタの自動アップグレードやメンテナンスアクティビティが実行されない期間を設定する機能です。これにより、特定の時間帯やイベント中にアップグレードを回避できます。

## Changed
原文:
 **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.33.4-gke.1134000 is now the default version for cluster creation.
- The following versions are now available:

- 1.30.14-gke.1267000
- 1.31.12-gke.1220000
- 1.32.9-gke.1010000
- 1.33.4-gke.1350000

- The following node versions are now available:

- 1.28.15-gke.2697000
- 1.29.15-gke.1936000
- 1.30.14-gke.1267000
- 1.31.12-gke.1220000
- 1.32.9-gke.1010000
- 1.33.4-gke.1350000

- The following versions are no longer available:

- 1.30.14-gke.1011000
- 1.31.12-gke.1060000
- 1.32.7-gke.1079000

- Auto-upgrade targets are now available for the following minor versions:

- Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version 1.30.14-gke.1108000 with this release.

- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:

- Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version 1.30.14-gke.1108000 with this release.
- Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version 1.33.4-gke.1134000 with this release.

[1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
- 1.30.14-gke.1267000
- 1.31.12-gke.1220000
- 1.32.9-gke.1010000
- 1.33.4-gke.1350000

[1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
[1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
[1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
[1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
- 1.28.15-gke.2697000
- 1.29.15-gke.1936000
- 1.30.14-gke.1267000
- 1.31.12-gke.1220000
- 1.32.9-gke.1010000
- 1.33.4-gke.1350000

[1.28.15-gke.2697000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
[1.29.15-gke.1936000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
[1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
[1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
[1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
[1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
- 1.30.14-gke.1011000
- 1.31.12-gke.1060000
- 1.32.7-gke.1079000

- Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version 1.30.14-gke.1108000 with this release.

[1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)
- Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version 1.30.14-gke.1108000 with this release.
- Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version 1.33.4-gke.1134000 with this release.

[1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
[1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)

説明：
クラスタ作成時のデフォルトバージョンが `1.33.4-gke.1134000` に更新されました。また、複数のGKEバージョン（コントロールプレーンおよびノードの両方）が新たに利用可能になり、一部の古いバージョンは利用不可となりました。自動アップグレードが有効なクラスタは、指定されたターゲットバージョン（例: 1.29から1.30.14へのマイナーバージョンアップグレード、または既存のマイナーバージョンに対するパッチアップグレード）にアップグレードされます。

影響有無：
*   **新規クラスタ**: クラスタを作成する際、デフォルトで `1.33.4-gke.1134000` が選択されます。
*   **既存クラスタ**: 自動アップグレードが有効なGKEクラスタは、記載されたターゲットバージョンにアップグレードが実行されます。特に、