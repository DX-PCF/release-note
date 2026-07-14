
# Title: July 13, 2026 
Link: https://docs.cloud.google.com/release-notes#July_13_2026<br>
はい、承知いたしました。Google Cloudのリリースノートに基づき、BigQueryに関するセキュリティ情報について調査し、ご提示いただいた形式で回答いたします。

---

# BigQuery

## Security

原文:
A Missing Authorization vulnerability was discovered in repositories in
BigQuery, Dataform, and Colab Enterprise. An authenticated attacker could
potentially escalate permissions and perform cross-tenant repository takeover.
For more information, see the
GCP-2026-047 security bulletin.
[GCP-2026-047](https://docs.cloud.google.com/support/bulletins#gcp-2026-047)

説明：
BigQuery、Dataform、およびColab Enterpriseの各サービスで使用されるリポジトリにおいて、「認証の欠落」に関する脆弱性（GCP-2026-047）が発見されました。この脆弱性が悪用された場合、すでに認証済みの攻撃者が権限を昇格させ、別のテナントのリポジトリを不正に制御下に置く可能性がありました。

影響有無：
**影響あり**（過去）。
お客様がBigQuery、Dataform、またはColab Enterpriseのリポジトリ機能を利用している場合、過去にこの脆弱性の影響を受ける可能性がありました。
しかし、この脆弱性はGoogle Cloudによって既に特定され、**修正済み（Patched）**です。Google Cloudのサービス側でパッチが適用されているため、現在お客様のサービスがこの脆弱性によって影響を受けることはありません。

対処方法：
**対処は不要です。**
Google Cloudが既にこの脆弱性に対してサービス側でパッチを適用済みであり、お客様側での追加の対応は必要ありません。GCP-2026-047のセキュリティ速報にも「Remediation: No customer action is required.（お客様側でのアクションは不要です）」と明記されています。

用語説明：
*   **Missing Authorization vulnerability（認証の欠落脆弱性）**: アプリケーションやシステムが、ユーザーが特定の操作を実行する前に、そのユーザーがその操作を行う権限を持っているかを適切に確認しない場合に発生するセキュリティ上の欠陥。これにより、本来許可されていない操作が実行される可能性があります。
*   **Authenticated attacker（認証された攻撃者）**: すでにシステムに対して何らかの有効な認証情報（例：ユーザー名とパスワード）を持っている攻撃者。この脆弱性は、認証された攻撃者が本来持つべき権限を超えて不正な操作を行うことを可能にするものです。
*   **Escalate permissions（権限昇格）**: 認証されたユーザーが、本来アクセスできないはずのリソースや機能にアクセスしたり、本来持たないはずの管理権限などを取得したりすること。セキュリティ上の重大な問題です。
*   **Cross-tenant repository takeover（テナントを越えたリポジトリ乗っ取り）**: マルチテナント環境（複数の顧客が同じインフラストラクチャを共有するクラウド環境）において、あるテナントの攻撃者が、別のテナントのリポジトリ（コード、設定ファイル、データなどが含まれる場所）を不正に制御下に置くこと。
*   **Security bulletin（セキュリティ速報）**: ベンダー（この場合はGoogle Cloud）が、自社製品やサービスで発見された、または報告されたセキュリティ脆弱性に関する公式な情報提供。脆弱性の内容、影響、重要度、および対処状況（パッチの有無、ユーザーが取るべき行動など）が記載されます。
# Title: July 10, 2026 
Link: https://docs.cloud.google.com/release-notes#July_10_2026<br>
ご担当者様

Google Cloud のリリースノートに基づき、お客様のGoogle Cloud Composer 2.7.1環境への影響調査結果を以下の通りご報告いたします。

---

# Google Kubernetes Engine

## Change

原文: GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.
[GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)
## No channel (deprecated)
**Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- The following versions are now available:
    - 1.33.13-gke.1101000
    - 1.34.9-gke.1287000
    - 1.35.6-gke.1250000
    - 1.36.0-gke.4681000
    - 1.36.2-gke.1346000
- The following node versions are now available:
    - 1.30.14-gke.2816000
    - 1.31.14-gke.2233000
    - 1.32.13-gke.1913000
    - 1.33.13-gke.1101000
    - 1.34.9-gke.1287000
    - 1.35.6-gke.1250000
    - 1.36.0-gke.4681000
    - 1.36.2-gke.1346000
    ... (Kubernetes CHANGELOG links omitted for brevity)

説明：
Google Kubernetes Engine (GKE) において、特定のリリースチャネルに属さない（"No channel"）GKEクラスタおよびノードの新しいバージョンが、手動アップグレードおよび新規クラスタ作成向けに利用可能になりました。これらのバージョンには、Kubernetesの機能改善やバグ修正、パフォーマンス向上が含まれています。

影響有無：**影響なし（直接的）**
理由：お客様がご利用のGoogle Cloud Composerは、Googleによって管理されるGKEクラスタを基盤としており、通常は特定のリリースチャネル（StableまたはRegular）に属するバージョンが適用されます。Composer環境において、基盤GKEクラスタの手動アップグレードは推奨されておらず、Composerの自動メンテナンスまたはComposer環境自体のアップグレードによってGKEバージョンが管理されるため、この「No channel」の変更が直接的な影響を及ぼすことはありません。

対処方法：
特段の対応は不要です。Composerの基盤GKEバージョンは、Composerサービスによって自動的に管理・更新されます。

---

## Security

原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release. To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the **Security** release notes for that image. The following table includes links to the release notes for each updated Container-Optimized OS image:
| GKE version | Container-Optimized OS version | Details |
| --- | --- | --- |
| 1.31.14-gke.2233000 | cos-117-18613-613-77 | [cos-117-18613-613-77 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-613-77_) |
| 1.32.13-gke.1913000 | cos-117-18613-613-77 | [cos-117-18613-613-77 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-613-77_) |
| 1.33.13-gke.1101000 | cos-121-18867-381-201 | [cos-121-18867-381-201 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121#cos-121-18867-381-201_) |
| 1.34.9-gke.1287000 | cos-125-19216-395-138 | [cos-125-19216-395-138 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m125#cos-125-19216-395-138_) |
| 1.36.0-gke.4681000 | cos-129-19506-224-80 | [cos-129-19506-224-80 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m129#cos-129-19506-224-80_) |

説明：
今回のGKEリリースには、セキュリティ修正が適用された最新のContainer-Optimized OS (COS) イメージが組み込まれています。これらのイメージは、過去のGKEリリース以降に公開された全てのCOSバージョンのセキュリティ修正を累積的に含んでおり、GKEクラスタの基盤となるOSレベルのセキュリティが強化されます。

影響有無：**影響あり（ポジティブ）**
理由：お客様がご利用のGoogle Cloud Composer環境の基盤となるGKEクラスタも、将来的にこれらのセキュリティ修正が適用されたContainer-Optimized OSイメージを使用するGKEバージョンに自動または半自動でアップグレードされる可能性があります。これにより、システムのセキュリティ体制が向上し、潜在的な脆弱性に対する防御が強化されます。

対処方法：
特段の緊急対応は不要です。Composerの自動メンテナンス機能により、基盤となるGKEのセキュリティアップデートが適用されます。ただし、アップグレードに備えて、既存のワークロードが新しいGKEバージョンでも問題なく動作するかをテスト環境で確認することを推奨します。

---

## Change

原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- The following versions are now available in the Stable channel:
    - 1.33.12-gke.1165000
    - 1.34.8-gke.1278000
    ... (Kubernetes CHANGELOG links omitted for brevity)

説明：
GKEのStableチャネルで、新しいバージョン `1.33.12-gke.1165000` および `1.34.8-gke.1278000` が利用可能になりました。Stableチャネルは、Google Cloudが十分なテストを行った上で提供する、最も安定性の高いGKEバージョンを提供するチャネルです。

影響有無：**影響あり（間接的）**
理由：Google Cloud Composerは、通常StableチャネルのGKEバージョンを基盤として使用します。現在ご利用中のComposer 2.7.1環境の基盤となるGKEクラスタは、Composerの自動メンテナンス機能を通じて、将来的にこれらの新しいStableバージョンのいずれかにアップグレードされる可能性があります。これにより、GKEの安定性向上や新機能の恩恵を受けられることが期待されます。

対処方法：
直接的な対応は不要です。GKEのマイナーバージョンアップグレード（例: 1.33から1.34）では、Kubernetes APIの変更や非推奨化が発生する可能性があるため、Composer環境のメンテナンスウィンドウ中に自動アップグレードが行われる前に、テスト環境で現在のDAGsやカスタムプラグインが新しいGKEバージョンで正常に動作するか検証することを推奨します。

---

## Change

原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- The following versions are now available in the Regular channel:
    - 1.33.12-gke.1270000
    - 1.34.9-gke.1065000
    - 1.35.6-gke.1049000
    - 1.36.0-gke.3302004
    - 1.36.0-gke.3712000
    ... (Kubernetes CHANGELOG links omitted for brevity)

説明：
GKEのRegularチャネルで、新しいバージョン `1.33.12-gke.1270000`、`1.34.9-gke.1065000`、`1.35.6-gke.1049000`、`1.36.0-gke.3302004`、`1.36.0-gke.3712000` が利用可能になりました。Regularチャネルは、Stableチャネルよりも新しい機能が早く提供され、安定性と新機能のバランスが良いチャネルです。

影響有無：**影響あり（間接的）**
理由：Google Cloud Composerは、Stableチャネルに加えてRegularチャネルのGKEバージョンも基盤として使用する場合があります。現在ご利用中のComposer 2.7.1環境の基盤となるGKEクラスタは、Composerの自動メンテナンス機能を通じて、将来的にこれらの新しいRegularバージョンのいずれかにアップグレードされる可能性があります。

対処方法：
Stableチャネルと同様に、直接的な対応は不要ですが、GKEのマイナーバージョンアップグレード（例: 1.35から1.36）ではKubernetes APIの変更や非推奨化が発生する可能性があるため、Composer環境のメンテナンスウィンドウ中に自動アップグレードが行われる前に、テスト環境で現在のDAGsやカスタムプラグインが新しいGKEバージョンで正常に動作するか検証することを推奨します。

---

