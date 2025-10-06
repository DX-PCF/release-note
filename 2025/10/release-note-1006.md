
# Title: October 02, 2025 
Link: https://cloud.google.com/release-notes#October_02_2025<br>
# Google Kubernetes Engine

## Changed

原文:
**Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

- Version 1.33.4-gke.1245000 is now the default version for cluster creation in the Extended channel.
- The following versions are now available in the Extended channel:
    - 1.28.15-gke.2697000
    - 1.28.15-gke.2740000
    - 1.29.15-gke.1936000
    - 1.29.15-gke.1979000
    - 1.30.14-gke.1267000
    - 1.31.12-gke.1220000
    - 1.32.9-gke.1010000
    - 1.33.4-gke.1350000
- The following versions are no longer available in the Extended channel:
    - 1.28.15-gke.2610000
    - 1.28.15-gke.2730000
    - 1.29.15-gke.1835000
    - 1.29.15-gke.1971000
    - 1.30.14-gke.1130000
    - 1.31.12-gke.1110000
    - 1.32.8-gke.1134000
    - 1.33.4-gke.1172000
- Auto-upgrade targets are now available for the following minor versions:
    - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version 1.28.15-gke.2630000 with this release.
- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
    - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version 1.28.15-gke.2630000 with this release.
    - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version 1.29.15-gke.1851000 with this release.
    - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version 1.30.14-gke.1150000 with this release.
    - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version 1.32.8-gke.1170000 with this release.
    - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version 1.33.4-gke.1245000 with this release.

説明：
ExtendedチャネルにおけるGKEのバージョン更新に関するアナウンスです。新規クラスター作成時のデフォルトバージョンが1.33.4-gke.1245000に変更されました。また、利用可能なGKEバージョンが追加され、一部の古いバージョンが利用不可となりました。自動アップグレードが有効な既存クラスターについては、マイナーバージョンアップグレード（例: 1.27から1.28へのアップグレード）および、メンテナンス除外設定などでマイナーバージョンアップグレードができないクラスター向けのパッチバージョンアップグレードの新しいターゲットが設定されました。

影響有無：
影響あり。
1.  **新規クラスター**: Extendedチャネルで新規にGKEクラスターを作成する場合、デフォルトで1.33.4-gke.1245000が選択されます。意図するバージョンと異なる場合は、明示的にバージョンを指定する必要があります。
2.  **既存クラスター**:
    *   **バージョン削除**: 利用不可となったバージョン（例: 1.28.15-gke.2610000）を使用しているクラスターは、サポート期間が終了する前にサポート対象バージョンへのアップグレードが必要です。
    *   **自動アップグレード**: Extendedチャネルで自動アップグレードが有効になっているGKEクラスター、またはGoogle Cloud Composer 2.7.1（基盤GKEがExtendedチャネルに設定されている場合）は、メンテナンスウィンドウ中に記載されたターゲットバージョンにアップグレードされます。特にマイナーバージョンアップグレード（1.27 -> 1.28）は、Kubernetes APIの変更や非推奨機能により、既存のワークロードに影響を与える可能性があります。
3.  **Google Cloud Composer 2**: Composer 2.7.1環境の基盤GKEがExtendedチャネルで運用されている場合、GKEの自動アップグレードによりバージョンが更新される可能性があります。通常、Google Cloud側で互換性が検証されていますが、AirflowのカスタムプラグインやタスクがGKEの特定のバージョンに依存している場合は、アップグレード後の動作確認が推奨されます。

対処方法：
1.  新規GKEクラスター作成時は、`gcloud container clusters create` コマンドやGCP Consoleで明示的にGKEバージョンを指定し、意図しないバージョンで作成されないよう確認してください。
2.  利用不可となったバージョンを使用している既存クラスターは、早急にサポート対象のGKEバージョンへのアップグレードを計画・実施してください。
3.  自動アップグレードが有効な既存GKEクラスターやComposer環境では、ターゲットとなるGKEバージョン（特にマイナーバージョンアップグレード）において、既存のアプリケーションやAirflowワークフローが正常に動作するか、事前に検証環境で互換性テストを実施することを推奨します。
4.  GKEクラスターの[メンテナンスウィンドウとメンテナンス除外](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions)設定を確認し、アップグレードのタイミングを制御してください。

用語説明：
*   **Extended channel**: GKEのリリースチャネルの一つ。より長い期間特定のマイナーバージョンがサポートされるが、Rapid/Regularチャネルよりも更新頻度が低い。
*   **自動アップグレード**: GKEが自動的にコントロールプレーンとノードを新しいバージョンにアップグレードする機能。
*   **メンテナンス除外 (Maintenance Exclusions)**: GKEクラスタのアップグレードやその他のメンテナンス作業を特定の期間避けるための設定。
*   **コントロールプレーン (Control Plane)**: Kubernetesクラスターの頭脳であり、APIサーバー、スケジューラー、コントローラーマネージャーなどが含まれる。
*   **ノード (Node)**: Kubernetesクラスター内でワークロード（Pod）を実行するワーカーマシン。

## Changed

原文:
**Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

- Version 1.33.4-gke.1245000 is now the default version for cluster creation.
- The following versions are now available:
    - 1.30.14-gke.1325000
    - 1.31.13-gke.1008000
    - 1.32.9-gke.1092000
    - 1.33.5-gke.1125000
- The following node versions are now available:
    - 1.28.15-gke.2740000
    - 1.29.15-gke.1979000
    - 1.30.14-gke.1325000
    - 1.31.13-gke.1008000
    - 1.32.9-gke.1092000
    - 1.33.5-gke.1125000
- The following versions are no longer available:
    - 1.30.14-gke.1059000
    - 1.31.12-gke.1110000
    - 1.32.6-gke.1025000
    - 1.33.3-gke.1136000
- Auto-upgrade targets are now available for the following minor versions:
    - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version 1.30.14-gke.1150000 with this release.
    - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version 1.32.8-gke.1108000 with this release.
- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
    - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version 1.30.14-gke.1150000 with this release.
    - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version 1.32.8-gke.1108000 with this release.
    - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version 1.33.4-gke.1245000 with this release.

説明：
特定のチャネルが明示されていませんが、これはGKEクラスタ作成時のデフォルトバージョン、利用可能なコントロールプレーンおよびノードバージョン、そして自動アップグレードターゲットの一般的な更新を指します。新規クラスターのデフォルトバージョンが1.33.4-gke.1245000に変更され、利用可能なGKEバージョンが追加・削除されました。また、自動アップグレードが有効な既存クラスター向けの新しいターゲットバージョンが設定されました。これには、マイナーバージョンアップグレードと、メンテナンス除外設定などでマイナーバージョンアップグレードができないクラスター向けのパッチバージョンアップグレードのターゲットが含まれます。

影響有無：
影響あり。
1.  **新規クラスター**: 新規にGKEクラスターを作成する場合、デフォルトで1.33.4-gke.1245000が選択されます。意図するバージョンと異なる場合は、明示的にバージョンを指定する必要があります。
2.  **既存クラスター**:
    *   **バージョン削除**: 利用不可となったバージョン（例: 1.30.14-gke.105