
# Title: September 09, 2026 
Link: https://docs.cloud.google.com/release-notes#September_09_2026<br>
リリースノートのご提供ありがとうございます。

ご提示いただいたリリースノートは「# Cloud SDK ## Breaking」までで、具体的な変更内容が記載されておりません。そのため、現在の情報では構築済みのサービスへの影響有無を判断することができません。

恐れ入りますが、Cloud SDKにおける具体的なBreaking Changeの内容を追記していただくようお願いいたします。詳細なリリースノートが提供され次第、改めて影響調査を実施し、回答例に沿ってご報告させていただきます。

以下に、現時点での情報に基づく回答の枠組みを示します。

---

# Cloud SDK
## Breaking
**原文:** (具体的なリリースノートの記載がありません)

**説明:**
提供された情報には、Cloud SDKにおける「Breaking Change」のカテゴリのみが示されており、具体的な変更内容が記載されておりません。このため、どのような機能がどのように変更されたのか、あるいは削除されたのかを特定できません。

**影響有無:**
具体的な変更内容が不明であるため、現在の構成や利用中のサービスへの影響有無を判断することはできません。
一般的に、Cloud SDKのBreaking Changeは、コマンドラインインターフェース（gcloud CLI）の挙動変更、APIの非互換な変更、依存関係の更新などにより、既存のスクリプト、自動化ツール、または開発ワークフローに影響を及ぼす可能性があります。

**対処方法:**
具体的な変更内容が不明なため、現時点では特定の対処方法を提示することはできません。
リリースノートの具体的な記述が提供され次第、以下の点を考慮して対処方法を検討します。
*   **非互換な変更:** 利用しているgcloudコマンド、ライブラリ、APIに非互換な変更がないかを確認し、必要に応じてスクリプトやコードの修正を検討します。
*   **バージョンアップ計画:** Breaking Changeが含まれる場合は、本番環境への適用前に開発環境やステージング環境で十分なテストを実施し、互換性を確認することが不可欠です。
*   **代替手段の有無:** 変更された機能や削除された機能に対する代替手段が提供されているかを確認します。

**用語説明:**
*   **Cloud SDK:** Google Cloud Platform のサービスと対話するためのツールセットです。gcloud コマンドラインツール、各種クライアントライブラリ、エミュレータなどが含まれます。主に開発者や管理者によって、プログラムによる GCP リソースの管理や操作、アプリケーションの開発に利用されます。
*   **Breaking Change (破壊的変更):** ソフトウェアの新しいバージョンで導入される変更のうち、以前のバージョンとの互換性を失わせる変更のことです。これにより、既存のコード、設定、または操作手順が動作しなくなる可能性があります。APIの引数変更、関数の削除、デフォルト値の変更などが該当します。システムの安定稼働のためには、これらの変更への対応が不可欠です。
# Title: September 08, 2026 
Link: https://docs.cloud.google.com/release-notes#September_08_2026<br>
はい、Google Cloudのインフラエンジニアとして、ご提示いただいたGKEのリリースノートについて、構築済みのサービス（特にGoogle Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)）への影響有無を調査し、回答いたします。

---

# Google Kubernetes Engine

## Change

原文: GKE cluster versions have been updated.

 **New versions available for upgrades and new clusters.**

 The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see GKE versioning and
support and About GKE
cluster upgrades.

[GKE versioning and
support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE
cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)

説明: GKEクラスタのバージョンが更新され、新しいGKEクラスタの作成や、既存クラスタのコントロールプレーンおよびノードのアップグレードに利用可能なバージョンが追加されました。GKEのバージョン管理とアップグレードに関する詳細については、関連ドキュメントを参照してください。これは、全体的なバージョン更新のアナウンスです。

影響有無: 影響なし
これはGKEクラスタのバージョン更新に関する一般的なアナウンスであり、特定の機能変更や非互換性の導入を示すものではありません。後続の各リリースチャンネルにおける具体的なバージョン変更の前提となる情報提供です。

対処方法: なし

用語説明:
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するマネージドなKubernetesサービス。
*   **コントロールプレーン (Control Plane)**: Kubernetesクラスタの管理コンポーネント群（APIサーバー、スケジューラー、コントローラーマネージャーなど）を指します。
*   **ノード (Node)**: Kubernetesクラスタ内でコンテナ化されたアプリケーション（Pod）が実行される仮想マシンまたは物理マシン。

## Change

原文: **No channel (deprecated)**

 **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.35.7-gke.1222000 is now the default version for cluster creation.
- The following versions are now available:

- 1.34.11-gke.1056000
- 1.35.8-gke.1380000
- 1.36.4-gke.1247000

- The following node versions are now available:

- 1.31.14-gke.2689000
- 1.32.13-gke.2411000
- 1.33.13-gke.1636000
- 1.34.11-gke.1056000
- 1.35.8-gke.1380000
- 1.36.4-gke.1247000

- The following versions are no longer available:

- 1.34.10-gke.1079000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.7-gke.1027000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.36.3-gke.1537000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:

- 1.35 to 1.35.7-gke.1222000
- 1.36 to 1.36.3-gke.1640000

[1.35.7-gke.1222000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000)
[1.34.11-gke.1056000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)
[1.35.8-gke.1380000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)
[1.36.4-gke.1247000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-1247000)
[1.31.14-gke.2689000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.31#1-31-14-gke-2689000)
[1.32.13-gke.2411000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.32#1-32-13-gke-2411000)
[1.33.13-gke.1636000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.33#1-33-13-gke-1636000)
[1.34.11-gke.1056000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-11-gke-1056000)
[1.35.8-gke.1380000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1380000)
[1.36.4-gke.1247000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-4-gke-136-4-gke-1247000)
[deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support)
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)

説明: `No channel` におけるGKEのバージョン更新です。
*   `1.35.7-gke.1222000` がクラスタ作成時のデフォルトバージョンになりました。
*   新しい利用可能バージョン（コントロールプレーンおよびノード）が追加されました。
*   以下のバージョンは非推奨となり、90日以内、またはサポート終了時に削除されます: `1.34.10-gke.1079000`, `1.35.7-gke.1027000`, `1.36.3-gke.1537000`。
*   現在のマイナーバージョンを実行しているクラスタの自動アップグレードターゲットが更新され、パッチバージョンアップグレードの新しいターゲットが設定されました。

影響有無: なし (ただし、GKEクラスタ運用のベストプラクティスに従う場合)
*   **GKEクラスタ**: `No channel` は推奨されるリリースチャンネルではありません。通常、運用中のGKEクラスタはStable、Regular、Rapid、またはExtendedチャンネルのいずれかに登録されています。もし意図せず `No channel` で運用しているGKEクラスタがあり、かつ非推奨バージョン (`1.34.10-gke.1079000`, `1.35.7-gke.1027000`, `1.36.3-gke.1537000`) を使用している場合は、90日以内に強制アップグレードされるため、速やかにサポートされているバージョンへのアップグレードが必要です。
*   **Google Cloud Composer2**: Composer2はマネージドサービスであり、基盤となるGKEクラスタのバージョンはGoogle Cloudによって管理され、通常は推奨されるリリースチャンネル（StableまたはRegular）のGKEバージョンが適用されます。`No channel` をComposerが利用することは極めて稀であり、またComposer 2.7.1 (Airflow 2.7.3) のサポートGKEバージョンは通常1.27.xまたは1.28.x系であり、本リリースノートのバージョン帯 (1.31-1.36系) とは異なります。そのため、直接的な影響は無いと判断されます。

対処方法:
*   **GKEクラスタ**: 現在 `No channel` のGKEクラスタを運用している場合は、[GKEリリースチャンネル](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels)のドキュメントを参照し、推奨されるリリースチャンネルへの移行を強く検討してください。非推奨バージョンを使用している場合は、直ちにサポートされているバージョンへのアップグレードを計画し、実行してください。
*   **Google Cloud Composer2**: 通常、Composer2ユーザーによる特別な対処は不要です。ComposerのGKEバージョンは自動的に管理され、必要なアップグレードはメンテナンスウィンドウ内で実行されます。

用語説明:
*   **リリースチャンネル (Release Channels)**: GKEクラスタのバージョンアップグレードの頻度や安定性レベルを定義する仕組み。`No channel` は特定のチャンネルに属さず、手動管理が前提となるため非推奨とされています。
*   **デフォルトバージョン (Default Version)**: 新しいクラスタを作成する際にデフォルトで選択されるGKEバージョン。
*   **利用可能バージョン (Available Versions)**: 新規クラスタ作成やアップグレードで選択可能なGKEバージョン。
*   **利用不可バージョン (No Longer Available Versions)**: 今後利用できなくなるバージョン。これには、Deprecatedとされた後に削除されるバージョンも含まれます。
*   **Deprecatedバージョン (Deprecated Versions)**: 非推奨とされたバージョン。一定期間後にサポートが終了し、利用できなくなります。通常、代替手段への移行期間が設けられます。
*   **自動アップグレードターゲット (Auto-upgrade targets)**: GKEが自動アップグレードを行う際の目標となるバージョン。メンテナンスウィンドウの設定などにより、アップグレードのタイミングを制御できます。
*   **パッチバージョン (Patch Version)**: Kubernetesバージョン番号 `X.Y.Z` の `Z` の部分。バグ修正やセキュリティパッチなどの軽微な変更が含まれます。
*   **マイナーバージョン (Minor Version)**: Kubernetesバージョン番号 `X.Y.Z` の `Y` の部分。新機能の追加やAPI変更など、互換性が維持される範囲での機能追加が含まれます。

## Security

原文: This release includes new GKE versions that use updated
Container-Optimized OS images. These updated images are cumulative,
incorporating security fixes from all Container-Optimized OS
versions released since the previous GKE release.

 To identify the specific vulnerabilities that were resolved in each updated
Container-Optimized OS image, see the **Security** release notes
for that image. The following table includes links to the release notes for
each updated Container-Optimized OS image:

 GKE version
Container-Optimized OS version
Details


1.31.14-gke.2689000
cos-117-18613-731-2
cos-117-18613-731-2 release notes


1.36.4-gke.1247000
cos-129-19506-448-8
cos-129-19506-448-8 release notes


1.37.0-gke.3165000
cos-129-19506-299-82
cos-129-19506-299-82 release notes

| GKE version | Container-Optimized OS version | Details |
| --- | --- | --- |
| 1.31.14-gke.2689000 | cos-117-18613-731-2 | cos-117-18613-731-2 release notes |
| 1.36.4-gke.1247000 | cos-129-19506-448-8 | cos-129-19506-448-8 release notes |
| 1.37.0-gke.3165000 | cos-129-19506-299-82 | cos-129-19506-299-82 release notes |
[cos-117-18613-731-2 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-731-2_)
[cos-129-19506-448-8 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m129#cos-129-19506-448-8_)
[cos-129-19506-299-82 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m129#cos-129-19506-299-82_)

説明: このリリースには、セキュリティ修正が適用されたContainer-Optimized OS (COS) イメージを使用する新しいGKEバージョンが含まれています。これらのイメージは、前回のGKEリリース以降に公開されたCOSのすべてのセキュリティ修正を累積的に含んでいます。特定の脆弱性情報は、各COSイメージのリリースノートで確認できます。

影響有無: ポジティブな影響
*   **GKEクラスタ/Google Cloud Composer2**: セキュリティ脆弱性が修正された新しいCOSイメージがGKEノードに適用されるため、クラスタ全体のセキュリティ体制が向上します。これは既存のワークロードにプラスの影響を与えます。Composer2も基盤のGKEノードイメージが更新されるため、セキュリティが強化されます。

対処方法:
*   **GKEクラスタ**: 最新のセキュリティ修正を適用するため、GKEクラスタを最新の利用可能なバージョンにアップグレードすることを検討してください。自動アップグレードが有効な場合でも、メンテナンスウィンドウの設定を確認し、適切なタイミングでアップグレードが実施されることを確認してください。
*   **Google Cloud Composer2**: Composer2はマネージドサービスであるため、基盤となるGKEノードのCOSイメージは自動的に更新されます。ユーザー側での特別な対処は不要ですが、セキュリティ体制が強化されたことを認識しておくと良いでしょう。

用語説明:
*   **Container-Optimized OS (COS)**: Google Cloud向けに最適化された、コンテナ実行に特化したオペレーティングシステム。GKEノードのデフォルトOSとして利用されます。
*   **セキュリティ修正 (Security Fixes)**: ソフトウェアの脆弱性（セキュリティホール）を修復するためのパッチや更新。

## Change

原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.34.10-gke.1106000 is now available in the Stable channel.
- Version 1.34.10-gke.1079000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

[1.34.10-gke.1106000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1106000)
[deprecated](https://docs.cloud.com/kubernetes-engine/versioning#patch-version-support)

説明: StableチャネルにおけるGKEのバージョン更新です。
*   `1.34.10-gke.1106000` がStableチャネルで利用可能になりました。
*   `1.34.10-gke.1079000` はStableチャネルで非推奨となり、90日以内、またはサポート終了時に削除されます。

影響有無: なし (ただし、該当バージョンを利用中の場合、対処が必要)
*   **GKEクラスタ**: StableチャネルでGKEクラスタを運用しており、かつ非推奨バージョン (`1.34.10-gke.1079000`) を使用している場合は、90日以内に強制アップグレードされるため、速やかにサポートされているバージョンへのアップグレードが必要です。
*   **Google Cloud Composer2**: Composer 2.7.1 (Airflow 2.7.3) のサポートGKEバージョンは通常1.27.xまたは1.28.x系であり、本リリースノートのバージョン帯 (1.34系) とは異なります。そのため、直接的な影響は無いと判断されます。ただし、将来的にComposerがこれらのバージョン帯に移行した場合や、特殊な設定でこのStableチャネルバージョンを利用している場合は、注意が必要です。

対処方法:
*   **GKEクラスタ**: Stableチャネルで稼働しているGKEクラスタのバージョンが `1.34.10-gke.1079000` である場合は、サポートされている新しいバージョン (`1.34.10-gke.1106000` など) へのアップグレードを計画し、実行してください。
*   **Google Cloud Composer2**: 通常、Composer2ユーザーによる特別な対処は不要です。ComposerのGKEバージョンは自動的に管理され、必要なアップグレードはメンテナンスウィンドウ内で実行されます。

## Change

原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.35.7-gke.1222000 is now the default version for cluster creation in the Regular channel.
- The following versions are now available in the Regular channel:

- 1.34.10-gke.1328000
- 1.35.8-gke.1036000
- 1.36.3-gke.1767000

- The following versions are no longer available in the Regular channel:

- 1.34.10-gke.1106000
- 1.35.7-gke.1150000
- 1.36.3-gke.1537000 is deprecated in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:

- 1.33 to 1.34.10-gke.1236000
- 1.34 to 1.35.7-gke.1222000

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:

- 1.34 to 1.34.10-gke.1236000
- 1.35 to 1.35.7-gke.1222000
- 1.36 to 1.36.3-gke.1640000

[1.35.7-gke.1222000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-7-gke-1222000)
[1.34.10-gke.1328000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.34#1-34-10-gke-1328000)
[1.35.8-gke.1036000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.35#1-35-8-gke-1036000)
[1.36.3-gke.1767000](https://docs.cloud.google.com/kubernetes-engine/docs/changelogs/1.36#1-36-3-gke-1767000)
[deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support)
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/