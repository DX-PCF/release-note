
# Title: August 15, 2025 
Link: https://cloud.google.com/release-notes#August_15_2025<br>
# Cloud SQL for PostgreSQL
## Deprecated
原文: You can no longer set a deny maintenance period for instances that are running a maintenance version older than 12 months. To update your instance, perform self-service maintenance or wait until the next maintenance window to update your instance automatically. For more information about maintenance, see Maintenance updates on Cloud SQL instances.

説明：
Cloud SQL for PostgreSQLにおいて、12ヶ月以上前のメンテナンスバージョンで稼働しているインスタンスに対し、メンテナンス拒否期間（deny maintenance period）を設定する機能が廃止されました。これは、インスタンスを最新の状態に保ち、セキュリティパッチや重要なバグ修正を適用することを目的としています。対象となるインスタンスは、手動でセルフサービスメンテナンスを実行するか、次回のメンテナンスウィンドウで自動的にアップデートされる必要があります。

影響有無：
**影響あり**
現在運用中のCloud SQL for PostgreSQLインスタンスの中に、メンテナンスバージョンが12ヶ月以上古いものが存在する場合、そのインスタンスに対してはメンテナンス拒否期間を設定できなくなります。これにより、意図しないタイミングでのメンテナンス（再起動を伴う可能性あり）が発生するリスクがあります。アプリケーションの可用性要件が高い場合、影響を十分に考慮する必要があります。

対処方法：
1.  **現状確認**: 運用中のCloud SQL for PostgreSQLインスタンスのメンテナンスバージョンを確認し、12ヶ月以上前のバージョンで稼働しているインスタンスがないか特定します。
2.  **メンテナンス戦略の見直し**: 該当するインスタンスが存在する場合、メンテナンス拒否期間に依存しないメンテナンス計画へ移行することを検討します。
3.  **計画的なアップデートの実施**: セルフサービスメンテナンス機能を利用し、業務影響の少ない時間帯に計画的にインスタンスを最新のメンテナンスバージョンに更新することを推奨します。これにより、メンテナンス拒否期間が設定できなくても、コントロールされたアップデートが可能です。
4.  **通知設定の確認**: メンテナンス通知が適切に担当者に届くように設定されていることを確認し、自動メンテナンスが実行される前に準備ができるようにします。

用語説明：
*   **メンテナンス拒否期間 (deny maintenance period)**: Cloud SQLインスタンスのメンテナンスウィンドウ設定の一部で、指定した期間内はメンテナンスアップデートの実行を拒否する設定です。通常、業務のピーク時間帯や特定のイベント期間中にインスタンスの再起動を避けるために利用されます。
*   **セルフサービスメンテナンス (self-service maintenance)**: Cloud SQLユーザーが任意のタイミングで、自身でメンテナンスアップデートの適用を開始できる機能です。これにより、ダウンタイムを許容できる特定の時間帯に計画的にメンテナンスを実施できます。
*   **メンテナンスバージョン (maintenance version)**: Cloud SQLインスタンスに適用される、マイナーバージョン内のパッチレベルやセキュリティ修正を示すバージョンです。定期的に更新され、パフォーマンス改善やセキュリティ脆弱性の修正などが含まれます。
# Title: August 14, 2025 
Link: https://cloud.google.com/release-notes#August_14_2025<br>
# Google Kubernetes Engine
## Changed
原文:
 **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- The following versions are now available in the Extended channel:
- 1.28.15-gke.2507000
- 1.28.15-gke.2547000
- 1.29.15-gke.1686000
- 1.29.15-gke.1756000
- 1.30.12-gke.1414000
- 1.31.11-gke.1036000
- 1.32.6-gke.1125000

- The following versions are no longer available in the Extended channel:
- 1.28.15-gke.2475000
- 1.28.15-gke.2527000
- 1.29.15-gke.1639000
- 1.29.15-gke.1713000
- 1.30.12-gke.1372000
- 1.31.10-gke.1067000
- 1.32.6-gke.1060000

- Auto-upgrade targets are now available for the following minor versions:
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version 1.28.15-gke.2488000 with this release.

- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version 1.28.15-gke.2488000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version 1.29.15-gke.1656000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version 1.30.12-gke.1390000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version 1.31.11-gke.1002000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version 1.32.6-gke.1096000 with this release.

説明：
Extendedチャネルにおいて、新しいGKEバージョンが利用可能になり、一部の古いバージョンが利用できなくなりました。また、自動アップグレードのターゲットバージョンが更新されました。これには、マイナーバージョンアップ（例：1.27から1.28へ）および、メンテナンス除外などの理由でマイナーバージョンアップができないクラスター向けのパッチバージョンアップターゲットが含まれます。

影響有無：
影響なし。
当社のGKEクラスターがExtendedチャネルを利用しており、自動アップグレードが有効な場合、設定されたメンテナンスウィンドウに従ってコントロールプレーンとノードが自動的に新しいバージョンにアップグレードされます。これは通常の運用プロセスであり、特別なアプリケーション変更の必要性は通常発生しません。Google Cloud Composer2 (Composer version 2.7.1、Airflow version 2.7.3)は、GKE上で動作しますが、本GKEバージョンのアップデート情報のみでは、Composerの動作に直接的な影響を与える変更は含まれていません。

対処方法：
自動アップグレードが有効な場合は、メンテナンスウィンドウと除外設定を確認し、アップグレードのスケジュールを把握してください。アップグレード前に、各バージョンのKubernetesチェンジログを確認し、アプリケーションとの互換性に懸念がないか確認することを推奨します。

用語説明：
*   **Extended channel**: GKEのリリースチャネルの一つで、長期サポート（LTS）を重視する環境向けに提供されます。他のチャネルよりもリリースサイクルが長く、より安定性が重視されます。
*   **自動アップグレード**: GKEクラスターのコントロールプレーンおよびノードが、Google Cloudによって自動的に最新の推奨バージョンに更新される機能です。
*   **メンテナンス除外 (Maintenance Exclusions)**: GKEのメンテナンスウィンドウ機能の一部で、特定の期間、自動アップグレードなどのメンテナンス作業を一時的に停止する設定です。

---

## Changed
原文:
 **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- The following versions are now available:
- 1.30.14-gke.1036000
- 1.31.11-gke.1101000
- 1.32.7-gke.1079000
- 1.33.3-gke.1250000
- 1.33.3-gke.1266000

- The following node versions are now available:
- 1.28.15-gke.2547000
- 1.29.15-gke.1756000
- 1.30.14-gke.1036000
- 1.31.11-gke.1101000
- 1.32.7-gke.1079000
- 1.33.3-gke.1250000
- 1.33.3-gke.1266000

- The following versions are no longer available:
- 1.30.12-gke.1333000
- 1.31.10-gke.1021000
- 1.32.4-gke.1767000

- Auto-upgrade targets are now available for the following minor versions:
- Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version 1.30.12-gke.1390000 with this release.
- Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version 1.31.11-gke.1002000 with this release.
- Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version 1.32.6-gke.1025000 with this release.

- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
- Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version 1.30.12-gke.1390000 with this release.
- Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version 1.31.11-gke.1002000 with this release.
- Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version 1.32.6-gke.1025000 with this release.

説明：
GKEのデフォルト（一般提供）バージョンとして、新しいバージョンが利用可能になり、一部の古いバージョンが利用できなくなりました。また、ノードプールで利用可能なバージョンも更新されました。自動アップグレードのターゲットバージョンが更新され、マイナーバージョンアップおよびパッチバージョンアップのターゲットが示されています。

影響有無：
影響なし。
当社のGKEクラスターがこれらのバージョンチャネルを利用しており、自動アップグレードが有効な場合、設定されたメンテナンスウィンドウに従ってコントロールプレーンとノードが自動的に新しいバージョンにアップグレードされます。これは通常の運用プロセスであり、特別なアプリケーション変更の必要性は通常発生しません。Google Cloud Composer2 (Composer version 2.7.1、Airflow version 2.7.3)は、GKE上で動作しますが、本GKEバージョンのアップデート情報のみでは、Composerの動作に直接的な影響を与える変更は含まれていません。

対処方法：
自動アップグレードが有効な場合は、メンテナンスウィンドウと除外設定を確認し、アップグレードのスケジュールを把握してください。アップグレード前に、各バージョンのKubernetesチェンジログを確認し、アプリケーションとの互換性に懸念がないか確認することを推奨します。

用語説明：
*   **ノードバージョン (Node Versions)**: GKEクラスタを構成するワーカーノード（コンテナが実際に動作するVM）上で動作するKubernetesのバージョンです。コントロールプレーンのバージョンとは独立して管理・アップグレードされる場合があります。

---

## Changed
原文:
 **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- The following versions are now available in the Rapid channel:
- 1.30.14-gke.1036000
- 1.31.11-gke.1101000
- 1.32.7-gke.1079000
- 1.33.3-gke.1250000
- 1.33.3-gke.1266000

- The following versions are no longer available in the Rapid channel:
- 1.30.12-gke.1390000
- 1.31.11-gke.1002000
- 1.32.6-gke.1096000

- Auto-upgrade targets are now available for the following minor versions:
- Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version 1.30.12-gke.1414000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version 1.31.11-gke.1036000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version 1.32.6-gke.1125000 with this release.

- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
- Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version 1.30.12-gke.1414000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version 1.31.11-gke.1036000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version 1.32.6-gke.1125000 with this release.

説明：
Rapidチャネルにおいて、新しいGKEバージョンが利用可能になり、一部の古いバージョンが利用できなくなりました。また、自動アップグレードのターゲットバージョンが更新されました。これには、マイナーバージョンアップおよびパッチバージョンアップのターゲットが含まれます。

影響有無：
影響なし。
当社のGKEクラスターがRapidチャネルを利用しており、自動アップグレードが有効な場合、設定されたメンテナンスウィンドウに従ってコントロールプレーンとノードが自動的に新しいバージョンにアップグレードされます。これは通常の運用プロセスであり、特別なアプリケーション変更の必要性は通常発生しません。Google Cloud Composer2 (Composer version 2.7.1、Airflow version 2.7.3)は、GKE上で動作しますが、本GKEバージョンのアップデート情報のみでは、Composerの動作に直接的な影響を与える変更は含まれていません。

対処方法：
Rapidチャネルは最も早く最新バージョンが提供されるため、頻繁なバージョン更新が予想されます。自動アップグレードが有効な場合は、メンテナンスウィンドウと除外設定を確認し、アップグレードのスケジュールを把握してください。継続的にKubernetesの変更履歴を確認し、アプリケーションとの互換性をテストする体制を整えることを推奨します。

用語説明：
*   **Rapid channel**: GKEのリリースチャネルの一つで、最新の機能や修正が最も早く導入されるチャネルです。開発環境や、最新機能を積極的に利用したい場合に適しています。

---

## Changed
原文:
 **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- The following versions are now available in the Regular channel:
- 1.30.12-gke.1414000
- 1.31.11-gke.1036000
- 1.32.6-gke.1125000

- The following versions are no longer available in the Regular channel:
- 1.30.12-gke.1372000
- 1.31.10-gke.1067000
- 1.32.6-gke.1060000

- Auto-upgrade targets are now available for the following minor versions:
- Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version 1.30.12-gke.1390000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version 1.31.11-gke.1002000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version 1.32.6-gke.1096000 with this release.

- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
- Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version 1.30.12-gke.1390000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version 1.31.11-gke.1002000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version 1.32.6-gke.1096000 with this release.

説明：
Regularチャネルにおいて、新しいGKEバージョンが利用可能になり、一部の古いバージョンが利用できなくなりました。また、自動アップグレードのターゲットバージョンが更新されました。これには、マイナーバージョンアップおよびパッチバージョンアップのターゲットが含まれます。

影響有無：
影響なし。
当社のGKEクラスターがRegularチャネルを利用しており、自動アップグレードが有効な場合、設定されたメンテナンスウィンドウに従ってコントロールプレーンとノードが自動的に新しいバージョンにアップグレードされます。これは通常の運用プロセスであり、特別なアプリケーション変更の必要性は通常発生しません。Google Cloud Composer2 (Composer version 2.7.1、Airflow version 2.7.3)は、GKE上で動作しますが、本GKEバージョンのアップデート情報のみでは、Composerの動作に直接的な影響を与える変更は含まれていません。

対処方法：
自動アップグレードが有効な場合は、メンテナンスウィンドウと除外設定を確認し、アップグレードのスケジュールを把握してください。アップグレード前に、各バージョンのKubernetesチェンジログを確認し、アプリケーションとの互換性に懸念がないか確認することを推奨します。

用語説明：
*   **Regular channel**: GKEのリリースチャネルの一つで、バランスの取れたリリース頻度と安定性を提供します。多くの本番環境で推奨されるチャネルです。

---

## Changed
原文:
 **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.32.6-gke.1025000 is now the default version for cluster creation in the Stable channel.
- The following versions are now available in the Stable channel:
- 1.30.12-gke.1372000
- 1.31.10-gke.1067000
- 1.32.6-gke.1060000

- The following versions are no longer available in the Stable channel:
- 1.30.12-gke.1333000
- 1.31.10-gke.1021000
- 1.32.6-gke.1013000

- Auto-upgrade targets are now available for the following minor versions:
- Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version 1.30.12-gke.1340000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version 1.31.10-gke.1034000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version 1.32.6-gke.1025000 with this release.

- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
- Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version 1.30.12-gke.1340000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version 1.31.10-gke.1034000 with this release.
- Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version 1.32.6-gke.1025000 with this release.

説明：
Stableチャネルにおいて、GKEバージョン `1.32.6-gke.1025000` がクラスター作成時のデフォルトバージョンになりました。また、新しいGKEバージョンが利用可能になり、一部の古いバージョンが利用できなくなりました。自動アップグレードのターゲットバージョンも更新されました。これには、マイナーバージョンアップおよびパッチバージョンアップのターゲットが含まれます。

影響有無：
影響なし。
当社のGKEクラスターがStableチャネルを利用しており、自動アップグレードが有効な場合、設定されたメンテナンスウィンドウに従ってコントロールプレーンとノードが自動的に新しいバージョンにアップグレードされます。これは通常の運用プロセスであり、特別なアプリケーション変更の必要性は通常発生しません。Google Cloud Composer2 (Composer version 2.7.1、Airflow version 2.7.3)は、GKE上で動作しますが、本GKEバージョンのアップデート情報のみでは、Composerの動作に直接的な影響を与える変更は含まれていません。

対処方法：
自動アップグレードが有効な場合は、メンテナンスウィンドウと除外設定を確認し、アップグレードのスケジュールを把握してください。新規にクラスターを作成する際は、デフォルトバージョンが変更されたことを認識しておいてください。アップグレード前に、各バージョンのKubernetesチェンジログを確認し、アプリケーションとの互換性に懸念がないか確認することを推奨します。

用語説明：
*   **Stable channel**: GKEのリリースチャネルの一つで、最も安定したバージョンを提供します。新しい機能の導入は慎重に行われ、長期的な安定稼働が重視されます。

---

## Changed
原文:
 GKE cluster versions have been updated.

 **New versions available for upgrades and new clusters.**

 The following Kubernetes versions are now available for new clusters and for
opt-in control plane upgrades and node upgrades for existing clusters. For more
information on versioning and upgrades, see GKE versioning and support
and Upgrades.

説明：
GKEクラスターのバージョンが更新され、新しいKubernetesバージョンが、新規クラスター作成時、および既存クラスターのコントロールプレーンやノードのアップグレードオプションとして利用可能になったという一般的なアナウンスです。GKEのバージョン管理とアップグレードに関する詳細情報へのリンクが提供されています。

影響有無：
影響なし。
これはGKEバージョン更新に関する一般的な通知であり、上記の各チャネルでの具体的な変更を総括するものです。このアナウンス自体が追加の直接的な影響をもたらすものではありません。

対処方法：
特になし。上記の各チャネルごとの影響と対処方法に従ってください。