
# Title: August 21, 2025 
Link: https://cloud.google.com/release-notes#August_21_2025<br>
以下は、提供されたリリースノートに基づいた、構築済みのサービスへの影響調査結果です。

---

# BigQuery

## Announcement

### 原文:
Starting September 25, 2025, the BigQuery Data Transfer Service for third-party SAAS and database connectors will update to a consumption-based pricing model. With this new pricing model, you will be charged based on the compute resources consumed by your data transfers, measured in slot-hours. For more information, see Data Transfer Service pricing. This pricing update applies to the following third-party connectors when they are generally available (GA):
- Facebook Ads
- MySQL
- Oracle
- PostgreSQL
- Salesforce
- Salesforce Marketing Cloud
- ServiceNow
- Other third-party connectors planned for future releases

### 説明:
2025年9月25日以降、BigQuery Data Transfer ServiceのサードパーティSaaSおよびデータベースコネクタの料金モデルが変更されます。新しい料金モデルでは、データ転送で消費される計算リソース（スロット時間）に基づいて課金される「消費ベース」となります。この料金変更は、Facebook Ads、MySQL、Oracle、PostgreSQL、Salesforce、Salesforce Marketing Cloud、ServiceNowなど、現在GA（一般提供）されている、または将来GAになるサードパーティコネクタに適用されます。

### 影響有無:
影響あり。
現在、BigQuery Data Transfer Serviceでリストアップされているサードパーティコネクタ（Facebook Ads, MySQL, Oracle, PostgreSQL, Salesforce, Salesforce Marketing Cloud, ServiceNowなど）のいずれかを利用している場合、2025年9月25日以降にデータ転送のコストが増減する可能性があります。利用していない場合は影響ありません。

### 対処方法:
1.  現在、該当するBigQuery Data Transfer Serviceのサードパーティコネクタを利用しているか確認してください。
2.  利用している場合、新しい料金モデル（スロット時間ベース）の詳細を[Data Transfer Service pricing](https://cloud.google.com/bigquery/pricing#section-5)で確認し、現在のデータ転送量に基づいて将来のコストへの影響を評価してください。
3.  必要に応じて、データ転送の最適化や代替手段の検討を始めることを推奨します。

### 用語説明:
*   **BigQuery Data Transfer Service**: BigQueryに様々な外部データソースからデータを自動的に転送・ロードするフルマネージドサービスです。
*   **Consumption-based pricing model (消費ベース料金モデル)**: サービスの使用量（この場合はデータ転送に消費される計算リソース）に応じて料金が発生する課金方式です。
*   **Slot-hours (スロット時間)**: BigQueryがクエリやデータ転送などの計算処理を実行するために使用する計算リソースの測定単位です。

---

# Google Kubernetes Engine

## Changed

### 原文:
GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following Kubernetes versions are now available for new clusters and for opt-in control plane upgrades and node upgrades for existing clusters. For more information on versioning and upgrades, see GKE versioning and support and Upgrades.

### 説明:
GKEクラスターのバージョンが更新され、新しいクラスターの作成や既存クラスターのコントロールプレーンおよびノードのアップグレードに利用可能なバージョンが追加されました。

### 影響有無:
間接的な影響がある可能性があります。
構築済みのGoogle Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)はGKE上で動作するマネージドサービスであり、そのGKE基盤のバージョンはGoogle Cloudによって管理されます。この変更は、将来Composerの基盤となるGKEバージョンが自動アップグレードされる際の参照情報となります。現時点での直接的な影響はありません。

### 対処方法:
現時点でユーザーが直接対処すべきことはありません。Composerの基盤GKEバージョンアップグレードはGoogle Cloudによって行われます。将来的にComposerのメジャーバージョンアップグレードや特定のGKEバージョンへの追従がアナウンスされた際に、アプリケーション互換性などを確認することが推奨されます。

---

## Changed

### 原文:
Starting in GKE 1.33.3-gke.1136000, the validation of the HealthCheckPolicy CRD is now performed earlier by GKE Gateway. Hence, certain invalid policies are now rejected by `kubectl`. The resulting error message will specify why the policy is invalid.

### 説明:
GKE 1.33.3-gke.1136000以降のバージョンで、GKE Gatewayにおける`HealthCheckPolicy`カスタムリソース定義（CRD）のバリデーション（検証）がより早期に行われるようになりました。これにより、不正な設定を含むポリシーは`kubectl`コマンド実行時に拒否されるようになり、エラーメッセージで具体的な問題点が示されます。

### 影響有無:
影響は低いですが、可能性はあります。
Google Cloud Composerはマネージドサービスであり、通常、ユーザーが直接GKE Gatewayを使用したり、カスタムの`HealthCheckPolicy` CRDを詳細に定義・デプロイしたりすることは稀です。そのため、既存のComposer環境に直接影響を与える可能性は低いと考えられます。
しかし、もし何らかの理由でGKE Gatewayをカスタマイズして利用しており、かつGKEバージョンが1.33.3-gke.1136000以降にアップグレードされた場合、既存の不正な`HealthCheckPolicy`が拒否され、デプロイや更新に失敗する可能性があります。現在のComposer 2.7.1が使用しているGKEバージョンがこの変更対象より古い場合は、直ちには影響しません。

### 対処方法:
1.  現在のGoogle Cloud Composer環境がGKE Gatewayを使用しているか、およびカスタムの`HealthCheckPolicy` CRDをデプロイしているか確認してください。
2.  もし該当する場合、Google Cloud Composerの基盤GKEがバージョン1.33.3-gke.1136000以降にアップグレードされる前に、既存の`HealthCheckPolicy` CRDが有効な形式であることを確認し、必要に応じて修正することを推奨します。

### 用語説明:
*   **GKE Gateway**: Google Kubernetes EngineでKubernetes Gateway APIの機能を提供するコンポーネントで、高度なトラフィック管理機能（ルーティング、ロードバランシングなど）を可能にします。
*   **CRD (Custom Resource Definition)**: Kubernetesの機能を拡張し、ユーザーが独自のカスタムリソースを定義できるようにするメカニズムです。これにより、Kubernetes APIをカスタムオブジェクトで拡張できます。
*   **HealthCheckPolicy**: サービスやアプリケーションのヘルスチェックに関する設定を定義するポリシーです。

---

## Changed

### 原文:
**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

- The following versions are now available in the Extended channel:
  - 1.28.15-gke.2527000
  - 1.28.15-gke.2564000
  - 1.29.15-gke.1713000
  - 1.29.15-gke.1773000
  - 1.30.14-gke.1011000
  - 1.31.11-gke.1064000
  - 1.32.7-gke.1016000
  - 1.33.3-gke.1136000
- The following versions are no longer available in the Extended channel:
  - 1.28.15-gke.2488000
  - 1.28.15-gke.2547000
  - 1.29.15-gke.1656000
  - 1.29.15-gke.1756000
  - 1.30.12-gke.1390000
  - 1.31.11-gke.1002000
  - 1.32.6-gke.1096000
- Auto-upgrade targets are now available for the following minor versions:
  - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version 1.28.15-gke.2507000 with this release.
- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
  - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version 1.28.15-gke.2507000 with this release.
  - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version 1.29.15-gke.1686000 with this release.
  - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version 1.30.12-gke.1414000 with this release.
  - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version 1.31.11-gke.1036000 with this release.
  - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version 1.32.6-gke.1125000 with this release.

### 説明:
GKEのExtendedリリースチャネルにおいて、利用可能なGKEバージョンが更新され、いくつかの新しいバージョンが利用可能になり、古いバージョンが利用不可になりました。また、自動アップグレードが有効なクラスターのコントロールプレーンおよびノードについて、特定のマイナーバージョンからのアップグレードターゲット（例: 1.27から1.28.15-gke.2507000）が設定されました。パッチバージョンのみのアップグレードターゲットも更新されています。

### 影響有無:
間接的な影響がある可能性があります。
Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)はGKE上で動作するマネージドサービスであり、そのGKE基盤のバージョンはGoogle Cloudによって管理されます。ComposerがこのExtendedチャネルを使用している可能性は低いですが、GKEのバージョン管理の動向を示す情報となります。現時点での直接的な影響はありません。

### 対処方法:
現時点でユーザーが直接対処すべきことはありません。Composerの基盤GKEバージョンアップグレードはGoogle Cloudによって行われます。

---

## Changed

### 原文:
**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

- The following versions are now available:
  - 1.30.14-gke.1059000
  - 1.31.11-gke.1135000
  - 1.31.12-gke.1014000
  - 1.32.8-gke.1005000
  - 1.32.8-gke.1026000
  - 1.33.3-gke.1392000
  - 1.33.4-gke.1036000
- The following node versions are now available:
  - 1.28.15-gke.2564000
  - 1.29.15-gke.1773000
  - 1.30.14-gke.1059000
  - 1.31.11-gke.1135000
  - 1.31.12-gke.1014000
  - 1.32.8-gke.1005000
  - 1.32.8-gke.1026000
  - 1.33.3-gke.1392000
  - 1.33.4-gke.1036000
- The following versions are no longer available:
  - 1.30.12-gke.1340000
  - 1.31.10-gke.1034000
  - 1.32.6-gke.1013000
  - 1.33.1-gke.1584000
  - 1.33.3-gke.1250000
  - 1.33.3-gke.1266000
- Auto-upgrade targets are now available for the following minor versions:
  - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version 1.30.12-gke.1414000 with this release.
  - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version 1.31.11-gke.1036000 with this release.
  - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version 1.32.6-gke.1060000 with this release.
- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
  - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version 1.30.12-gke.1414000 with this release.
  - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version 1.31.11-gke.1036000 with this release.
  - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version 1.32.6-gke.1060000 with this release.

### 説明:
GKEにおいて、利用可能なGKEバージョンが更新され、いくつかの新しいバージョンが利用可能になり、古いバージョンが利用不可になりました。また、コントロールプレーンおよびノードの自動アップグレードターゲットが設定され、特定のマイナーバージョンからのアップグレードや、メンテナンス除外などによりマイナーバージョンアップグレードがブロックされているクラスターのパッチバージョンアップグレードターゲットが更新されました。

### 影響有無:
間接的な影響がある可能性があります。
Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)はGKE上で動作するマネージドサービスであり、そのGKE基盤のバージョンはGoogle Cloudによって管理されます。この変更は、将来Composerの基盤となるGKEバージョンが自動アップグレードされる際の参照情報となります。現時点での直接的な影響はありません。

### 対処方法:
現時点でユーザーが直接対処すべきことはありません。Composerの基盤GKEバージョンアップグレードはGoogle Cloudによって行われます。

---

## Changed

### 原文:
**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

- Version 1.33.3-gke.1136000 is now the default version for cluster creation in the Rapid channel.
- The following versions are now available in the Rapid channel:
  - 1.30.14-gke.1059000
  - 1.31.11-gke.1135000
  - 1.31.12-gke.1014000
  - 1.32.8-gke.1005000
  - 1.32.8-gke.1026000
  - 1.33.3-gke.1392000
  - 1.33.4-gke.1036000
- The following versions are no longer available in the Rapid channel:
  - 1.30.12-gke.1414000
  - 1.31.11-gke.1036000
  - 1.32.6-gke.1125000
  - 1.33.2-gke.1240000
  - 1.33.3-gke.1250000
  - 1.33.3-gke.1266000
- Auto-upgrade targets are now available for the following minor versions:
  - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version 1.30.14-gke.1011000 with this release.
  - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version 1.31.11-gke.1064000 with this release.
  - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version 1.32.7-gke.1016000 with this release.
  - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version 1.33.3-gke.1136000 with this release.
- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
  - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version 1.30.14-gke.1011000 with this release.
  - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version 1.31.11-gke.1064000 with this release.
  - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version 1.32.7-gke.1016000 with this release.
  - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version 1.33.3-gke.1136000 with this release.

### 説明:
GKEのRapidリリースチャネルにおいて、クラスター作成時のデフォルトバージョンが1.33.3-gke.1136000になりました。また、利用可能なGKEバージョンが更新され、いくつかの新しいバージョンが利用可能になり、古いバージョンが利用不可になりました。さらに、自動アップグレードが有効なクラスターのコントロールプレーンおよびノードについて、特定のマイナーバージョンからのアップグレードターゲットが設定され、パッチバージョンのみのアップグレードターゲットも更新されました。

### 影響有無:
間接的な影響がある可能性があります。
Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)はGKE上で動作するマネージドサービスであり、そのGKE基盤のバージョンはGoogle Cloudによって管理されます。ComposerがこのRapidチャネルを使用している可能性は低いですが、GKEのバージョン管理の動向を示す情報となります。現時点での直接的な影響はありません。

### 対処方法:
現時点でユーザーが直接対処すべきことはありません。Composerの基盤GKEバージョンアップグレードはGoogle Cloudによって行われます。

---

## Changed

### 原文:
**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

- The following versions are now available in the Regular channel:
  - 1.30.14-gke.1011000
  - 1.31.11-gke.1064000
  - 1.32.7-gke.1016000
  - 1.33.3-gke.1136000
- The following versions are no longer available in the Regular channel:
  - 1.30.12-gke.1390000
  - 1.31.11-gke.1002000
  - 1.32.6-gke.1096000
- Auto-upgrade targets are now available for the following minor versions:
  - Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version 1.30.12-gke.1414000 with this release.
  - Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version 1.31.11-gke.1036000 with this release.
  - Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version 1.32.6-gke.1125000 with this release.
- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
  - Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version 1.30.12-gke.1414000 with this release.
  - Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version 1.31.11-gke.1036000 with this release.
  - Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version 1.32.6-gke.1125000 with this release.

### 説明:
GKEのRegularリリースチャネルにおいて、利用可能なGKEバージョンが更新され、いくつかの新しいバージョンが利用可能になり、古いバージョンが利用不可になりました。また、自動アップグレードが有効なクラスターのコントロールプレーンおよびノードについて、特定のマイナーバージョンからのアップグレードターゲットが設定され、パッチバージョンのみのアップグレードターゲットも更新されました。

### 影響有無:
間接的な影響がある可能性があります。
Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)はGKE上で動作するマネージドサービスであり、そのGKE基盤のバージョンはGoogle Cloudによって管理されます。ComposerがRegularチャネルを使用している場合、これらのGKEバージョン情報がComposerの基盤の将来のアップグレードに影響を与える可能性があります。現時点での直接的な影響はありません。

### 対処方法:
現時点でユーザーが直接対処すべきことはありません。Composerの基盤GKEバージョンアップグレードはGoogle Cloudによって行われます。将来的にComposerのリリースノートで基盤GKEのバージョンアップグレードがアナウンスされた際には、Airflowやカスタムコンポーネントとの互換性を確認することが推奨されます。

---

## Changed

### 原文:
**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

- Version 1.32.6-gke.1060000 is now the default version for cluster creation in the Stable channel.
- The following versions are now available in the Stable channel:
  - 1.30.12-gke.1390000
  - 1.31.11-gke.1002000
  - 1.32.6-gke.1096000
- The following versions are no longer available in the Stable channel:
  - 1.30.12-gke.1340000
  - 1.31.10-gke.1034000
  - 1.32.6-gke.1025000
- Auto-upgrade targets are now available for the following minor versions:
  - Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version 1.30.12-gke.1372000 with this release.
  - Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version 1.31.10-gke.1067000 with this release.
