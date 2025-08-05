
# Title: August 01, 2025 
Link: https://cloud.google.com/release-notes#August_01_2025<br>
Google Cloud のリリースノートに基づき、構築済みのサービスへの影響を調査し、以下の通りご報告いたします。

---

# Google Kubernetes Engine (Extended チャネル)
## Changed
原文:
> **Note:** Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.
>
> - Version 1.33.2-gke.1240000 is now the default version for cluster creation in the Extended channel.
> - The following versions are now available in the Extended channel:
>   - 1.28.15-gke.2475000
>   - 1.28.15-gke.2507000
>   - 1.29.15-gke.1639000
>   - 1.29.15-gke.1686000
>   - 1.30.12-gke.1372000
>   - 1.31.10-gke.1067000
>   - 1.32.6-gke.1060000
> - The following versions are no longer available in the Extended channel:
>   - 1.28.15-gke.2456000
>   - 1.28.15-gke.2488000
>   - 1.29.15-gke.1607000
>   - 1.29.15-gke.1656000
>   - 1.30.12-gke.1333000
>   - 1.31.10-gke.1021000
>   - 1.32.6-gke.1013000
>   - 1.33.2-gke.1111000
> - Auto-upgrade targets are now available for the following minor versions:
>   - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version 1.28.15-gke.2461000 with this release.
> - The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
>   - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version 1.28.15-gke.2461000 with this release.
>   - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version 1.29.15-gke.1614000 with this release.
>   - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version 1.30.12-gke.1340000 with this release.
>   - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version 1.31.10-gke.1034000 with this release.
>   - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version 1.32.6-gke.1025000 with this release.
>   - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version 1.33.2-gke.1240000 with this release.

説明：
GKEのExtendedリリースチャネルにおいて、以下の変更がありました。
-   クラスター新規作成時のデフォルトバージョンが `1.33.2-gke.1240000` に更新されました。
-   複数のGKEバージョンがExtendedチャネルで利用可能になり、同時に複数のバージョンが利用不可になりました。
-   自動アップグレードのターゲットバージョンが更新され、Extendedチャネル内のクラスターは、マイナーバージョンアップグレードおよびパッチバージョンアップグレードが適用される可能性があります。特に、バージョン1.27のクラスターは1.28.15-gke.2461000へ、各マイナーバージョンのクラスターは最新のパッチバージョンへ自動アップグレードが開始されます。

影響有無：
**あり**
-   **GKEクラスター (Extendedチャネル利用中)**:
    -   自動アップグレードが有効化されている既存のGKEクラスターは、定義されたターゲットバージョンへのコントロールプレーンおよびノードのアップグレードが実施されます。特に、メンテナンス期間の設定や除外設定によっては、意図しないタイミングでアップグレードが開始される可能性があります。
    -   新規クラスターをExtendedチャネルで作成する場合、デフォルトバージョンが変更されるため、意識的にバージョンを指定しない限り新しいデフォルトバージョンでプロビジョニングされます。
    -   利用不可になったバージョンを使用しているクラスターは、今後のサポート計画に影響が出る可能性があります。
-   **Google Cloud Composer2 (Composer version 2.7.1、Airflow version 2.7.3)**:
    -   Composer環境の基盤であるGKEクラスターがExtendedチャネルを利用している場合、自動アップグレードの対象となる可能性があります。ただし、ComposerのGKEバージョンはComposerサービスによって管理されるため、ユーザーが直接GKEバージョンを操作することは通常ありません。Composerサービスは、基盤GKEのアップグレードプロセスと互換性を確認した上で適用するため、直接的な即時影響は限定的であると考えられますが、Composerの公式リリースノートやサポート対象GKEバージョンの情報も確認することを推奨します。

対処方法：
-   **GKEクラスター (Extendedチャネル利用中)**:
    -   現在運用中のGKEクラスターのバージョン、リリースチャネル、自動アップグレード設定、およびメンテナンスウィンドウ/除外設定を確認してください。
    -   自動アップグレードが有効な場合、アップグレードスケジュールを確認し、アプリケーションの互換性テストを事前に実施してください。特にマイナーバージョンアップグレード（1.27→1.28）は、APIの非互換性が含まれる可能性があるため、注意が必要です。
    -   利用不可になったバージョンを使用している場合は、早めにサポートされているバージョンへのアップグレードを計画してください。
    -   新規クラスター作成時は、意図するGKEバージョンを指定するようにしてください。
-   **Google Cloud Composer2**:
    -   Composer環境の基盤となるGKEクラスターのチャネルやバージョンは、通常Composerサービスが管理します。Composerのリリースノートやドキュメントを参照し、GKEのアップグレードに関するComposerの対応状況を確認してください。

用語説明：
-   **Extended チャネル**: GKEのリリースチャネルの一つで、Stableチャネルよりも新しいKubernetesバージョンを提供する一方で、より長い期間（通常はStableチャネルよりも長く）サポートされるパッチリリースを受け取ります。
-   **自動アップグレード (Auto-upgrade)**: GKEクラスターのコントロールプレーンおよびノードのKubernetesバージョンを自動的に更新する機能です。設定されたメンテナンスウィンドウ内で実行されます。
-   **メンテナンス除外 (Maintenance Exclusions)**: 特定の期間、GKEの自動メンテナンス（アップグレードを含む）を一時的に停止する設定です。これにより、重要なイベント期間中の予期せぬアップグレードを防ぐことができます。

---

# Google Kubernetes Engine (Default チャネル)
## Changed
原文:
> **Note:** Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.
>
> - Version 1.33.2-gke.1240000 is now the default version for cluster creation.
> - The following versions are now available:
>   - 1.30.12-gke.1414000
>   - 1.31.11-gke.1036000
>   - 1.32.6-gke.1125000
>   - 1.33.2-gke.4780000
> - The following node versions are now available:
>   - 1.28.15-gke.2507000
>   - 1.29.15-gke.1686000
>   - 1.30.12-gke.1414000
>   - 1.31.11-gke.1036000
>   - 1.32.6-gke.1125000
>   - 1.33.2-gke.4780000
> - The following versions are no longer available:
>   - 1.30.12-gke.1279000
>   - 1.31.9-gke.1218000
>   - 1.32.2-gke.1297002
>   - 1.32.4-gke.1415000
>   - 1.33.2-gke.4655000
> - Auto-upgrade targets are now available for the following minor versions:
>   - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version 1.30.12-gke.1340000 with this release.
>   - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version 1.31.10-gke.1034000 with this release.
>   - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version 1.32.4-gke.1767000 with this release.
> - The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
>   - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version 1.30.12-gke.1340000 with this release.
>   - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version 1.31.10-gke.1034000 with this release.
>   - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version 1.32.4-gke.1767000 with this release.
>   - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version 1.33.2-gke.1240000 with this release.

説明：
GKEのデフォルトリリースチャネル（またはチャネル指定なしのクラスター）において、以下の変更がありました。
-   クラスター新規作成時のデフォルトバージョンが `1.33.2-gke.1240000` に更新されました。
-   コントロールプレーンおよびノード向けに複数のGKEバージョンが利用可能になり、同時に複数のバージョンが利用不可になりました。
-   自動アップグレードのターゲットバージョンが更新され、自動アップグレードが有効化されているクラスターは、マイナーバージョンアップグレードおよびパッチバージョンアップグレードが適用される可能性があります。例えば、バージョン1.29のクラスターは1.30.12-gke.1340000へ、各マイナーバージョンのクラスターは最新のパッチバージョンへ自動アップグレードが開始されます。

影響有無：
**あり**
-   **GKEクラスター (デフォルトチャネルまたはチャネル指定なしのクラスター)**:
    -   自動アップグレードが有効化されている既存のGKEクラスターは、定義されたターゲットバージョンへのコントロールプレーンおよびノードのアップグレードが実施されます。
    -   新規クラスターをデフォルト設定で作成する場合、デフォルトバージョンが変更されるため、新しいデフォルトバージョンでプロビジョニングされます。
    -   利用不可になったバージョンを使用しているクラスターは、今後のサポート計画に影響が出る可能性があります。
-   **Google Cloud Composer2 (Composer version 2.7.1、Airflow version 2.7.3)**:
    -   Composer環境の基盤であるGKEクラスターがこのチャネルの挙動に従う場合、自動アップグレードの対象となる可能性があります。ComposerのGKEバージョンはComposerサービスによって管理されるため、直接的な即時影響は限定的であると考えられますが、Composerの公式リリースノートやサポート対象GKEバージョンの情報も確認することを推奨します。

対処方法：
-   **GKEクラスター (デフォルトチャネルまたはチャネル指定なしのクラスター)**:
    -   現在運用中のGKEクラスターのバージョン、自動アップグレード設定、およびメンテナンスウィンドウ/除外設定を確認してください。
    -   自動アップグレードが有効な場合、アップグレードスケジュールを確認し、アプリケーションの互換性テストを事前に実施してください。
    -   利用不可になったバージョンを使用している場合は、早めにサポートされているバージョンへのアップグレードを計画してください。
    -   新規クラスター作成時は、意図するGKEバージョンを指定するようにしてください。
-   **Google Cloud Composer2**:
    -   Composer環境の基盤となるGKEクラスターのチャネルやバージョンは、通常Composerサービスが管理します。Composerのリリースノートやドキュメントを参照し、GKEのアップグレードに関するComposerの対応状況を確認してください。

用語説明：
-   **デフォルトチャネル (Default channel)**: GKEでリリースチャネルを明示的に指定しない場合に適用される挙動です。GKEは内部的にStableチャネルに近い管理を行います。
-   **コントロールプレーン (Control Plane)**: Kubernetesクラスターの管理コンポーネント群（APIサーバー、etcd、スケジューラー、コントローラーマネージャーなど）を指します。
-   **ノード (Node)**: Kubernetesクラスターにおいて、コンテナ化されたアプリケーションを実行するワーカーマシンです。

---

# Google Kubernetes Engine (Rapid チャネル)
## Changed
原文:
> **Note:** Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.
>
> - The following versions are now available in the Rapid channel:
>   - 1.30.12-gke.1414000
>   - 1.31.11-gke.1036000
>   - 1.32.6-gke.1125000
>   - 1.33.2-gke.4780000
> - The following versions are no longer available in the Rapid channel:
>   - 1.30.12-gke.1340000
>   - 1.31.10-gke.1034000
>   - 1.32.6-gke.1025000
>   - 1.33.2-gke.4655000
> - Auto-upgrade targets are now available for the following minor versions:
>   - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version 1.30.12-gke.1372000 with this release.
>   - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version 1.31.10-gke.1067000 with this release.
>   - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version 1.32.6-gke.1060000 with this release.
> - The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
>   - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version 1.30.12-gke.1372000 with this release.
>   - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version 1.31.10-gke.1067000 with this release.
>   - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version 1.32.6-gke.1060000 with this release.

説明：
GKEのRapidリリースチャネルにおいて、以下の変更がありました。
-   複数のGKEバージョンがRapidチャネルで利用可能になり、同時に複数のバージョンが利用不可になりました。
-   自動アップグレードのターゲットバージョンが更新され、Rapidチャネル内のクラスターは、マイナーバージョンアップグレードおよびパッチバージョンアップグレードが適用される可能性があります。例えば、バージョン1.29のクラスターは1.30.12-gke.1372000へ、各マイナーバージョンのクラスターは最新のパッチバージョンへ自動アップグレードが開始されます。

影響有無：
**あり**
-   **GKEクラスター (Rapidチャネル利用中)**:
    -   自動アップグレードが有効化されている既存のGKEクラスターは、定義されたターゲットバージョンへのコントロールプレーンおよびノードのアップグレードが実施されます。Rapidチャネルは最新の機能が早く導入されるため、頻繁なアップグレードが予想されます。
    -   利用不可になったバージョンを使用しているクラスターは、今後のサポート計画に影響が出る可能性があります。
-   **Google Cloud Composer2 (Composer version 2.7.1、Airflow version 2.7.3)**:
    -   Composer環境の基盤であるGKEクラスターがRapidチャネルを利用している場合、自動アップグレードの対象となる可能性があります。Composerは通常、より安定したチャネルを利用しますが、もしRapidチャネルを使用している場合は、基盤GKEのアップグレード頻度が高くなるため、Composerの公式リリースノートやサポート対象GKEバージョンの情報に特に注意を払う必要があります。

対処方法：
-   **GKEクラスター (Rapidチャネル利用中)**:
    -   現在運用中のGKEクラスターのバージョン、リリースチャネル、自動アップグレード設定、およびメンテナンスウィンドウ/除外設定を確認してください。
    -   Rapidチャネルではアップグレードサイクルが速いため、アプリケーションの互換性テストプロセスを継続的に実施し、常に最新のKubernetesバージョンへの対応を考慮する必要があります。
    -   利用不可になったバージョンを使用している場合は、早めにサポートされているバージョンへのアップグレードを計画してください。
-   **Google Cloud Composer2**:
    -   Composer環境の基盤となるGKEクラスターのチャネルやバージョンは、通常Composerサービスが管理します。Composerのリリースノートやドキュメントを参照し、GKEのアップグレードに関するComposerの対応状況を確認してください。

用語説明：
-   **Rapid チャネル**: GKEのリリースチャネルの一つで、最新のKubernetesバージョンが最も早く提供されます。新しい機能や改善を早期に利用できますが、他のチャネルと比較してアップグレードの頻度が高く、リリースサイクルが速い傾向があります。

---

# Google Kubernetes Engine (Regular チャネル)
## Changed
原文:
> **Note:** Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.
>
> - Version 1.33.2-gke.1240000 is now the default version for cluster creation in the Regular channel.
> - The following versions are now available in the Regular channel:
>   - 1.30.12-gke.1372000
>   - 1.31.10-gke.1067000
>   - 1.32.6-gke.1060000
> - The following versions are no longer available in the Regular channel:
>   - 1.30.12-gke.1333000
>   - 1.31.10-gke.1021000
>   - 1.32.6-gke.1013000
>   - 1.33.2-gke.1111000
> - Auto-upgrade targets are now available for the following minor versions:
>   - Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version 1.30.12-gke.1340000 with this release.
>   - Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version 1.31.10-gke.1034000 with this release.
>   - Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version 1.32.6-gke.1025000 with this release.
> - The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
>   - Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version 1.30.12-gke.1340000 with this release.
>   - Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version 1.31.10-gke.1034000 with this release.
>   - Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version 1.32.6-gke.1025000 with this release.
>   - Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version 1.33.2-gke.1240000 with this release.

説明：
GKEのRegularリリースチャネルにおいて、以下の変更がありました。
-   クラスター新規作成時のデフォルトバージョンが `1.33.2-gke.1240000` に更新されました。
-   複数のGKEバージョンがRegularチャネルで利用可能になり、同時に複数のバージョンが利用不可になりました。
-   自動アップグレードのターゲットバージョンが更新され、Regularチャネル内のクラスターは、マイナーバージョンアップグレードおよびパッチバージョンアップグレードが適用される可能性があります。例えば、バージョン1.29のクラスターは1.30.12-gke.1340000へ、各マイナーバージョンのクラスターは最新のパッチバージョンへ自動アップグレードが開始されます。

影響有無：
**あり**
-   **GKEクラスター (Regularチャネル利用中)**:
    -   自動アップグレードが有効化されている既存のGKEクラスターは、定義されたターゲットバージョンへのコントロールプレーンおよびノードのアップグレードが実施されます。
    -   新規クラスターをRegularチャネルで作成する場合、デフォルトバージョンが変更されるため、新しいデフォルトバージョンでプロビジョニングされます。
    -   利用不可になったバージョンを使用しているクラスターは、今後のサポート計画に影響が出る可能性があります。
-   **Google Cloud Composer2 (Composer version 2.7.1、Airflow version 2.7.3)**:
    -   Composer環境の基盤であるGKEクラスターがRegularチャネルを利用している場合、自動アップグレードの対象となる可能性があります。Composerサービスは、基盤GKEのアップグレードプロセスと互換性を確認した上で適用するため、直接的な即時影響は限定的であると考えられますが、Composerの公式リリースノートやサポート対象GKEバージョンの情報も確認することを推奨します。ComposerはStableまたはRegularチャネルを利用することが一般的です。

対処方法：
-   **GKEクラスター (Regularチャネル利用中)**:
    -   現在運用中のGKEクラスターのバージョン、リリースチャネル、自動アップグレード設定、およびメンテナンスウィンドウ/除外設定を確認してください。
    -   自動アップグレードが有効な場合、アップグレードスケジュールを確認し、アプリケーションの互換性テストを事前に実施してください。
    -   利用不可になったバージョンを使用している場合は、早めにサポートされているバージョンへのアップグレードを計画してください。
    -   新規クラスター作成時は、意図するGKEバージョンを指定するようにしてください。
-   **Google Cloud Composer2**:
    -   Composer環境の基盤となるGKEクラスターのチャネルやバージョンは、通常Composerサービスが管理します。Composerのリリースノートやドキュメントを参照し、GKEのアップグレードに関するComposerの対応状況を確認してください。

用語説明：
-   **Regular チャネル**: GKEのリリースチャネルの一つで、Rapidチャネルよりも成熟したバージョンを提供し、Stableチャネルよりも早く新しい機能を利用できます。多くの本番環境で利用されるバランスの取れたチャネルです。

---

# Google Kubernetes Engine (Stable チャネル)
## Changed
原文:
> **Note:** Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.
>
> - Version 1.32.4-gke.1767000 is now the default version for cluster creation in the Stable channel.
> - The following versions are now available in the Stable channel:
>   - 1.30.12-gke.1333000
>   - 1.31.10-gke.1021000
>   - 1.32.6-gke.1013000
>   - 1.33.2-gke.1111000
> - The following versions are no longer available in the Stable channel:
>   - 1.30.12-gke.1279000
>   - 1.31.9-gke.1218000
>   - 1.32.4-gke.1698000
> - Auto-upgrade targets are now available for the following minor versions:
>   - Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version 1.30.12-gke.1320000 with this release.
>   - Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version 1.31.9-gke.1287000 with this release.
>   - Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version 1.32.4-gke.1767000 with this release.
> - The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
>   - Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version 1.30.12-gke.1320000 with this release.
>   - Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version 1.31.9-gke.1287000 with this release.
>   - Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version 1.32.4-gke.1767000 with this release.

説明：
GKEのStableリリースチャネルにおいて、以下の変更