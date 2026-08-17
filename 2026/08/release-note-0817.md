
# Title: August 14, 2026 
Link: https://docs.cloud.google.com/release-notes#August_14_2026<br>
承知いたしました。Google Kubernetes Engine (GKE) のリリースノートに基づき、貴社で構築済みのGoogle Cloud Composer2環境への影響を調査し、回答例に沿ってご報告いたします。

Google Cloud Composerはマネージドサービスであり、その基盤としてGoogle Kubernetes Engine (GKE) を利用しています。Composer環境のGKEバージョンは、Composerのバージョン（今回の場合 Composer 2.7.1）に紐付いており、通常、Google Cloudによって自動的に管理・アップグレードされます。そのため、GKEのバージョンアップデートは直接的な手動操作を必要としないことが多いですが、その変更がComposer環境の動作に間接的に影響を与える可能性について評価します。

---

# Google Kubernetes Engine

## Change (GKE cluster versions have been updated - No channel (deprecated))

**原文:**
GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.
[GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)
**Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.35.6-gke.1641000 is now the default version for cluster creation.
- The following versions are now available:
- 1.33.13-gke.1462000
- 1.34.10-gke.1106000
- 1.35.7-gke.1150000
- 1.36.3-gke.1537000
- The following node versions are now available:
- 1.31.14-gke.2579000
- 1.32.13-gke.2268000
- 1.33.13-gke.1462000
- 1.34.10-gke.1106000
- 1.35.7-gke.1150000
- 1.36.3-gke.1537000
- The following versions are no longer available:
- 1.33.13-gke.1011000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.34.8-gke.1278000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.34.9-gke.1287000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.5-gke.1057002 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.5-gke.1163012 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.5-gke.1241004 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.36.2-gke.1346000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.36.3-gke.1244000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.36.3-gke.1253000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
[deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support)
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
- 1.32 to 1.33.13-gke.1269000
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.33 to 1.33.13-gke.1269000
- 1.35 to 1.35.6-gke.1641000
- 1.36 to 1.36.2-gke.2064000
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)

**説明:**
GKEクラスタのバージョンが更新され、手動アップグレードや新規クラスタ作成で利用可能なバージョンが増えました。特に、バージョン1.35.6-gke.1641000がデフォルトになりました。また、いくつかの新しいパッチバージョンとノードバージョンが追加されています。一方で、複数のGKEバージョン（例: 1.33.13-gke.1011000、1.34.8-gke.1278000、1.35.5-gke.1057002など）が非推奨となり、90日以内に削除される予定です。GKEは、メンテナンス除外期間や非推奨APIの使用などの要因がなければ、指定されたマイナーバージョンまたはパッチバージョンへ自動アップグレードを行います。

**影響有無:**
**影響あり（軽微）**。
Google Cloud Composer 2.7.1は、その基盤としてGKEクラスタを使用しています。Composer環境のGKEバージョンは、Composerのバージョンに紐付いており、Google Cloudによって自動的に管理およびアップグレードされます。もし貴社のComposer環境が現在、非推奨となったGKEバージョンファミリーを使用している場合、今後90日以内に強制的に新しいサポート対象バージョンへ自動アップグレードされる可能性があります。新しいバージョンへのアップグレードは、セキュリティパッチやバグ修正が含まれるため、安定性向上が期待されますが、ごく稀に非互換性による動作変更が発生する可能性もゼロではありません。

**対処方法:**
1.  **GKEバージョンの確認:** 現在稼働しているComposer環境がどのGKEバージョンファミリーを使用しているかを確認してください。`gcloud composer environments describe` コマンドやGoogle Cloud Consoleから確認できます。
2.  **Composerのバージョンサポート確認:** Google Cloud Composerの公式ドキュメント [Google Cloud Composer supported versions](https://cloud.google.com/composer/docs/composer-2/supported-versions) を参照し、Composer 2.7.1がサポートするGKEバージョン範囲を確認してください。
3.  **自動アップグレードの監視:** 通常、Composer環境のGKEは自動アップグレードによって管理されます。特別なアクションは不要ですが、Composer環境のメンテナンスウィンドウ設定を確認し、アップグレードのタイミングを把握しておくことを推奨します。

**用語説明:**
*   **GKE (Google Kubernetes Engine):** Google Cloudが提供するマネージドなKubernetesサービス。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを自動化します。
*   **デフォルトバージョン:** 新規クラスタ作成時に、明示的にバージョンを指定しない場合に選択されるGKEのバージョン。
*   **非推奨 (Deprecated):** 今後のバージョンでサポートが終了する予定の機能やバージョン。この通知後90日以内に使用を停止し、代替バージョンへの移行が推奨されます。
*   **自動アップグレード (Auto-upgrade):** GKEクラスタのコントロールプレーンおよびノードが、Google Cloudによって自動的に新しいバージョンに更新される機能。これにより、セキュリティと安定性が維持されます。
*   **メンテナンス除外期間 (Maintenance Exclusions):** GKEクラスタの自動アップグレードやメンテナンス活動を一時的に停止する期間を設定する機能。
*   **コントロールプレーン (Control Plane):** Kubernetesクラスタを管理するコンポーネント群（APIサーバー、スケジューラー、コントローラーマネージャーなど）の総称。
*   **ノード (Node):** アプリケーションワークロードを実行する仮想マシンまたは物理マシン。Kubernetesクラスタ内のワーカーマシン。

---

## Security (Container-Optimized OS images)

**原文:**
This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release.
To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the **Security** release notes for that image. The following table includes links to the release notes for each updated Container-Optimized OS image:

| GKE version | Container-Optimized OS version | Details |
|---|---|---|
| 1.31.14-gke.2579000 | cos-117-18613-675-37 | cos-117-18613-675-37 release notes |
| 1.32.13-gke.2268000 | cos-117-18613-675-37 | cos-117-18613-675-37 release notes |
| 1.33.13-gke.1462000 | cos-121-18867-528-36 | cos-121-18867-528-36 release notes |
| 1.35.7-gke.1150000 | cos-125-19216-532-62 | cos-125-19216-532-62 release notes |
| 1.37.0-gke.1173000+preview | cos-129-19506-299-60 | cos-129-19506-299-60 release notes |

**説明:**
今回のGKEリリースには、更新されたContainer-Optimized OS (COS) イメージを使用するGKEバージョンが含まれています。これらのCOSイメージには、前回のGKEリリース以降にリリースされた全てのCOSバージョンからの累積的なセキュリティ修正が含まれています。各COSイメージで解決された特定の脆弱性については、対応するCOSのリリースノートで詳細を確認できます。

**影響有無:**
**影響なし（セキュリティ向上）**。
GKEノードが使用する基盤OSであるContainer-Optimized OSのセキュリティアップデートは、GKEクラスタ全体のセキュリティ体制を強化します。貴社のGoogle Cloud Composer環境のワーカーノードもこれらのCOSイメージを使用しているため、自動的なGKEバージョンアップグレードの一環として、セキュリティパッチが適用され、基盤のセキュリティが向上します。アプリケーションの互換性に対する直接的な悪影響は通常ありません。

**対処方法:**
特段の対処は不要です。GKEの自動アップグレードによって、これらのセキュリティ修正を含む新しいCOSイメージがノードに適用されます。

**用語説明:**
*   **Container-Optimized OS (COS):** Google Cloudが提供する、コンテナの実行に最適化された最小限のオペレーティングシステム。GKEノードのデフォルトOSとして使用されます。
*   **累積的なセキュリティ修正 (Cumulative security fixes):** 以前の全てのセキュリティ修正と今回の新しい修正をまとめたもの。

---

## Change (GKE cluster versions have been updated - Stable channel)

**原文:**
**Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.35.6-gke.1250000 is now the default version for cluster creation in the Stable channel.
- The following versions are now available in the Stable channel:
- 1.33.13-gke.1109000
- 1.34.9-gke.1322000
- The following versions are no longer available in the Stable channel:
- 1.33.13-gke.1011000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.34.9-gke.1287000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.5-gke.1057002 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.5-gke.1163012 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.5-gke.1241004 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
- 1.32 to 1.33.13-gke.1101000
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.33 to 1.33.13-gke.1101000
- 1.35 to 1.35.6-gke.1250000

**説明:**
StableチャネルにおけるGKEクラスタのバージョンが更新されました。バージョン1.35.6-gke.1250000がStableチャネルのデフォルトバージョンになりました。新しいパッチバージョンが追加され、同時にいくつかの旧バージョン（例: 1.33.13-gke.1011000、1.34.9-gke.1287000など）が非推奨となり、90日以内に削除される予定です。自動アップグレードのターゲットも更新され、クラスタは新しいマイナーバージョンやパッチバージョンへアップグレードされます。

**影響有無:**
**影響あり（軽微）**。
Google Cloud Composer環境は通常、StableチャネルまたはRegularチャネルに設定されています。Stableチャネルを利用しているComposer環境の基盤GKEクラスタは、今回の更新に伴い、新しいバージョンへ自動的にアップグレードされる可能性があります。非推奨となったバージョンを使用している場合は、計画的なアップグレードの対象となります。

**対処方法:**
「GKE cluster versions have been updated - No channel (deprecated)」の項目に記載されている対処方法と同様です。

**用語説明:**
*   **Stable チャネル (Stable Channel):** GKEのリリースチャネルの一つで、Googleによって徹底的にテストされ、安定性が重視されるバージョンが提供されます。本番環境での利用に推奨されます。

---

## Change (GKE cluster versions have been updated - Regular channel)

**原文:**
**Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.35.6-gke.1641000 is now the default version for cluster creation in the Regular channel.
- The following versions are now available in the Regular channel:
- 1.33.13-gke.1329000
- 1.34.9-gke.1655000
- 1.35.6-gke.1710000
- The following versions are no longer available in the Regular channel:
- 1.33.13-gke.1109000
- 1.34.9-gke.1322000
- 1.35.6-gke.1258000
- 1.36.2-gke.1346000 is deprecated in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
- 1.32 to 1.33.13-gke.1269000
- 1.33 to 1.34.9-gke.1610000
- 1.34 to 1.35.6-gke.1641000
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.33 to 1.33.13-gke.1269000
- 1.34 to 1.34.9-gke.1610000
- 1.35 to 1.35.6-gke.1641000
- 1.36 to 1.36.2-gke.2064000

**説明:**
RegularチャネルにおけるGKEクラスタのバージョンが更新されました。バージョン1.35.6-gke.1641000がRegularチャネルのデフォルトバージョンになりました。新しいパッチバージョンが追加され、同時にいくつかの旧バージョン（例: 1.33.13-gke.1109000、1.36.2-gke.1346000など）が非推奨となり、90日以内に削除される予定です。自動アップグレードのターゲットも更新され、クラスタは新しいマイナーバージョンやパッチバージョンへアップグレードされます。

**影響有無:**
**影響あり（軽微）**。
Google Cloud Composer環境は通常、StableチャネルまたはRegularチャネルに設定されています。Regularチャネルを利用しているComposer環境の基盤GKEクラスタは、今回の更新に伴い、新しいバージョンへ自動的にアップグレードされる可能性があります。非推奨となったバージョンを使用している場合は、計画的なアップグレードの対象となります。

**対処方法:**
「GKE cluster versions have been updated - No channel (deprecated)」の項目に記載されている対処方法と同様です。

**用語説明:**
*   **Regular チャネル (Regular Channel):** GKEのリリースチャネルの一つで、Stableチャネルよりも早く新機能やバージョンが提供されます。

---

## Change (GKE cluster versions have been updated - Rapid channel)

**原文:**
**Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- The following versions are now available in the Rapid channel:
- 1.33.13-gke.1462000
- 1.34.10-gke.1106000
- 1.35.7-gke.1150000
- 1.36.3-gke.1537000
- Alpha version 1.37.0-gke.1173000+preview is now available for GKE alpha clusters in the Rapid channel.
- The following versions are no longer available in the Rapid channel:
- 1.33.13-gke.1329000
- 1.34.9-gke.1655000
- 1.35.6-gke.1710000
- 1.36.3-gke.1244000 is deprecated in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.36.3-gke.1253000 is deprecated in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
- 1.32 to 1.33.13-gke.1414000
- 1.33 to 1.34.10-gke.1079000
- 1.34 to 1.35.7-gke.1027000
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.33 to 1.33.13-gke.1414000
- 1.34 to 1.34.10-gke.1079000
- 1.35 to 1.35.7-gke.1027000

**説明:**
RapidチャネルにおけるGKEクラスタのバージョンが更新されました。新しいパッチバージョンと、GKEアルファクラスタ向けにアルファ版1.37.0-gke.1173000+previewが利用可能になりました。同時にいくつかの旧バージョン（例: 1.33.13-gke.1329000、1.36.3-gke.1244000など）が非推奨となり、90日以内に削除される予定です。自動アップグレードのターゲットも更新され、クラスタは新しいマイナーバージョンやパッチバージョンへアップグレードされます。

**影響有無:**
**影響なし（ほとんどのComposer環境には関係なし）**。
Google Cloud Composer環境がRapidチャネルを使用していることは稀です。通常、本番環境ではStableまたはRegularチャネルが推奨されます。もし貴社のComposer環境がRapidチャネルを使用している場合は、GKEの自動アップグレードによって基盤クラスタのバージョンが更新される可能性があります。

**対処方法:**
Composer環境がRapidチャネルを使用していない限り、特段の対処は不要です。Rapidチャネルを使用している場合は、「GKE cluster
# Title: August 13, 2026 
Link: https://docs.cloud.google.com/release-notes#August_13_2026<br>
Google Cloud のインフラエンジニアとして、Apigee X のリリースノートについて調査しました。

---

# Apigee X

## Announcement
原文: On August 13th, 2026, we began maintenance updates of Apigee instances configured for maintenance windows.
[configured for maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows)
If you set a preferred window for maintenance for your instance, and your instance version is
below **1-18-0-apigee-2**, your instance will be updated to **1-18-0-apigee-2** within the
next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.

Note: Instances that meet either of the following two criteria will not be updated:

- Your instance has a DNS misconfiguration, as described in Known Issue 445936920.
- Your instance uses an Apigee Java Library that has been removed, as described in Apigee release notes dated October 16, 2025.

[Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues)
[Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025)
For more information on participating in scheduled maintenance windows, see Maintenance overview and Manage Apigee instance maintenance windows.

[Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance)
[Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows)

説明:
2026年8月13日から、メンテナンスウィンドウを設定しているApigeeインスタンスに対するメンテナンスアップデートが開始されました。もしお客様のインスタンスがメンテナンスの優先ウィンドウを設定しており、かつバージョンが **1-18-0-apigee-2** 未満の場合、今後7〜21日以内に **1-18-0-apigee-2** へアップデートされます。アップデート予定日を含む通知が今後2営業日以内に送信されます。
ただし、以下のいずれかの条件に該当するインスタンスはアップデートされません。
*   Known Issue 445936920に記載されているように、インスタンスにDNS設定ミスがある場合。
*   2025年10月16日のApigeeリリースノートに記載されている、削除されたApigee Java Libraryを使用している場合。

影響有無:
**影響あり**:
*   メンテナンスウィンドウを設定しているApigeeインスタンスがあり、かつ現在のバージョンが `1-18-0-apigee-2` 未満の場合、Google Cloudによって自動的にこのバージョンにアップデートされます。これにより、設定されたメンテナンスウィンドウ中にインスタンスが再起動し、短時間のAPIダウンタイムが発生する可能性があります。
*   アップデート対象となるインスタンスは、新しい機能や修正が適用されます。
**影響なし**:
*   メンテナンスウィンドウを設定していないApigeeインスタンス、または既に `1-18-0-apigee-2` 以上のバージョンであるインスタンスには直接的な影響はありません。
*   DNS設定ミスがある、または削除されたApigee Java Libraryを使用しているインスタンスは、このアップデートの対象外となります。

対処方法:
1.  メンテナンスウィンドウを設定しているApigeeインスタンスがある場合は、今後2営業日以内に送信される通知を確認し、アップデートの具体的な予定日を把握してください。
2.  アップデートによる影響を最小限に抑えるため、本番環境への適用前に開発/ステージング環境でAPIの動作確認を実施することを強く推奨します。
3.  もしインスタンスがDNS設定ミスや削除されたJava Libraryの使用によりアップデートされない場合は、これらの問題を解決することで、将来のメンテナンスアップデートを円滑に適用できるようになります。

用語説明:
*   **Apigeeインスタンス**: Google Cloud Apigee X API 管理サービスのデプロイ単位です。
*   **メンテナンスウィンドウ**: Google CloudがApigeeインスタンスに対してメンテナンス作業を行う時間帯を顧客が指定できる機能です。これにより、サービスの可用性への影響を最小限に抑えることができます。
*   **DNS misconfiguration (DNS設定ミス)**: Apigeeインスタンスのネットワーク設定において、Domain Name System (DNS) の解決に誤りがある状態を指します。

---

## Announcement
原文: On August 13th, 2026, we released an updated version of Apigee (1-18-0-apigee-3).

> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明:
2026年8月13日に、Apigeeの更新バージョン **1-18-0-apigee-3** がリリースされました。このリリースのロールアウトは本日開始され、すべてのGoogle Cloudゾーンで完了するまでに4営業日以上かかる場合があります。ロールアウトが完了するまで、お客様のインスタンスでは新機能や修正が利用できない場合があります。

影響有無:
**影響あり**:
*   お客様のApigeeインスタンスは、順次この最新バージョンである `1-18-0-apigee-3` にアップデートされます。これにより、後述の「Fixed」および「Security」セクションに記載されている修正と新機能が適用されます。
*   ロールアウト期間中（数営業日）は、すべてのゾーンで最新バージョンが利用可能になるまでに時間差が生じる可能性があります。
**影響なし**:
*   このアナウンス単体では、既存のAPIや構成に直接的な非互換性のある変更（Breaking Change）は示唆されていません。

対処方法:
1.  特段の対処は不要ですが、ご自身のApigeeインスタンスがいつ最新バージョンに更新されるかを把握するため、Apigee UIやCloud Logging等でインスタンスのバージョンを確認しておくと良いでしょう。
2.  新機能や修正の適用状況を確認し、必要に応じて利用計画を立ててください。

用語説明:
*   **Rollout (ロールアウト)**: 新しいソフトウェアバージョンや機能が、システム全体に段階的に展開され、適用されるプロセスを指します。

---

## Fixed
原文:
| Bug ID | Description |
|---|---|
| **532147587** | To fix forward proxy support. |
| **537657987** | Fixed a bug where watcher failed to reconcile all routes if an environment was not found in the control plane. |
| **543022076** | Google Cloud BOM upgrade (protobuf 4.x, gRPC 1.81, Guava 33.5). One user-visible change: a malformed inbound gRPC request frame is now reported to the client as grpc-status INTERNAL(13) and recorded in analytics as x-apigee.grpc.status=13, where it was previously an Apigee ServiceUnavailable fault seen as UNAVAILABLE(14) with no x-apigee.grpc.status recorded. Otherwise no user facing impact, but any prod issue related to gcp, protobuf or gRPC may relate to this. |
| **542242046** | Fixed LLMTokenQuota metering the request against an arbitrary quota bucket when the API Product declared multiple models and the request carried no model. |
| **531731614** | Apigee analytics fields ai_llm_response_token_count, ai_llm_prompt_token_count, ai_llm_model_name, and ai_llm_model_provider are available in the Custom Report when LLMTokenQuota and PromptTokenLimit policies are used in Apigee proxies. |
| **492044413** | LLMTokenQuota resolves the model from the API Product LLM Operation when LLMModelSource is omitted and the request body has no model field. |
| **67169710** | Adds an opt-in <DynamicClientIdSupported> boolean XML element to the OAuthV2 policy. When true, AbstractOAuthStepExecution.extractClientDetails() preserves any non-empty ClientID/ClientSecret already present on the OAuthClientContext. |
| **531731614** | Apigee auto identifies the providers and publishes them to analytics. |
| **537396574** | Added feature to rotate the apigee-ca certificate. |
| **540861752** | Aligned the ApigeeDeployment conversion hub with its v1alpha3 storage version. Internal change; no effect on existing ApigeeDeployment resources. |
| **540861752** | Aligned the ApigeeDeployment custom resource's conversion hub with its v1alpha3 storage version. This internal change does not affect existing ApigeeDeployment resources. |
| **N/A** | Updates to infrastructure and libraries. |

説明:
以下のバグ修正と機能改善が行われました。
*   **フォワードプロキシのサポート修正 (532147587)**: フォワードプロキシ機能のサポートが修正されました。
*   **ルート調停バグ修正 (537657987)**: コントロールプレーンで環境が見つからない場合にウォッチャーがすべてのルートを調停できないバグが修正されました。
*   **Google Cloud BOMアップグレード (543022076)**: protobuf (4.x)、gRPC (1.81)、Guava (33.5) など、Google Cloudの主要ライブラリがアップグレードされました。これにより、不正なgRPCリクエストフレームがクライアントに `grpc-status INTERNAL(13)` として報告され、アナリティクスに `x-apigee.grpc.status=13` と記録されるよう変更されました。以前は `ServiceUnavailable(14)` として報告され、`x-apigee.grpc.status` は記録されませんでした。
*   **LLMTokenQuotaの改善 (542242046, 492044413)**:
    *   API Productが複数のモデルを宣言しているにも関わらずリクエストにモデルが含まれていない場合に、LLMTokenQuotaが任意のクォータバケットに対してリクエストを計測してしまうバグが修正されました。
    *   `LLMModelSource` が省略され、リクエストボディにモデルフィールドがない場合、LLMTokenQuotaがAPI ProductのLLM Operationからモデルを解決するようになりました。
*   **LLMアナリティクスフィールドの追加と改善 (531731614)**: LLMTokenQuotaおよびPromptTokenLimitポリシーがApigeeプロキシで使用されている場合、カスタムレポートで `ai_llm_response_token_count`、`ai_llm_prompt_token_count`、`ai_llm_model_name`、`ai_llm_model_provider` のアナリティクスフィールドが利用可能になりました。また、Apigeeがプロバイダを自動的に識別し、アナリティクスに公開するようになりました。
*   **OAuthV2ポリシーの機能追加 (67169710)**: OAuthV2ポリシーにオプトインの `<DynamicClientIdSupported>` ブール型XML要素が追加されました。これを`true`に設定すると、AbstractOAuthStepExecution.extractClientDetails()がOAuthClientContextに既に存在するClientID/ClientSecretを保持するようになります。
*   **Apigee CA証明書ローテーション機能 (537396574)**: `apigee-ca` 証明書をローテーションする機能が追加されました。
*   **ApigeeDeploymentの内部変更 (540861752)**: ApigeeDeploymentの変換ハブがv1alpha3ストレージバージョンと整合するよう調整されました。これは内部的な変更であり、既存のApigeeDeploymentリソースには影響しません。
*   **インフラストラクチャとライブラリの更新 (N/A)**: インフラストラクチャとライブラリの一般的な更新が行われました。

影響有無:
**影響あり**:
*   **gRPCエラーハンドリングの変更 (543022076)**: Apigee経由でgRPC APIを利用している場合、不正なリクエストフレームのエラー報告方法が変更されます。これまで `ServiceUnavailable(14)` が返されていた状況で `INTERNAL(13)` が返されるようになり、アナリティクスに `x-apigee.grpc.status=13` が記録されるようになります。もしこれらのエラーコードに依存したカスタムロジックや監視システムがある場合、影響を受ける可能性があります。
*   **LLMアナリティクスフィールドの追加 (531731614)**: LLM関連のポリシー（LLMTokenQuota, PromptTokenLimit）を使用している場合、より詳細なメトリクスがカスタムレポートで利用可能になります。これは機能強化であり、既存のレポートに影響はありませんが、新しい分析の機会を提供します。
*   **OAuthV2ポリシーの機能追加 (67169710)**: OAuthV2ポリシーで動的なクライアントIDの処理が必要な場合に、新しいオプションを有効にすることで機能拡張が可能です。既存の動作には影響しません。
**影響なし**:
*   その他の多くの修正はバグ修正や内部的な改善であり、既存のApigeeワークロードに直接的な悪影響を与える可能性は低いと考えられます。
*   `apigee-ca` 証明書ローテーション機能は、必要に応じて手動で実行する機能であり、自動的に既存の証明書が変更されるわけではありません。

対処方法:
1.  **gRPCエラーハンドリングの変更 (543022076) について**:
    *   Apigee経由でgRPC APIを公開している、または利用している場合、gRPCリクエストの不正なフレームに関するエラーコードのハンドリングロジック（特に `ServiceUnavailable` をチェックしている箇所）を見直し、`INTERNAL(13)` に対応できるよう修正を検討してください。
    *   gRPCエラーのアナリティクス監視を行っている場合、新しい `x-apigee.grpc.status` フィールドの利用を検討し、より詳細な情報を取得するように更新してください。
2.  **LLMアナリティクスフィールド (531731614) について**: LLM関連のポリシーを利用している場合、これらの新しいフィールドを活用して、より詳細なAPI利用状況のカスタムレポートを生成することを検討してください。
3.  **OAuthV2ポリシーの機能追加 (67169710) について**: 動的なクライアントIDの処理が必要な場合は、OAuthV2ポリシーの定義に `<DynamicClientIdSupported>true</DynamicClientIdSupported>` を追加してこの新機能を有効にすることを検討してください。
4.  その他、もし特定のバグに影響を受けていた場合は、今回の修正により問題が解消されたことを確認してください。

用語説明:
*   **Forward Proxy (フォワードプロキシ)**: クライアントからのネットワークリクエストを中継し、外部ネットワークへのアクセスを代理するサーバーです。
*   **Control Plane (コントロールプレーン)**: Apigeeの管理層であり、APIのデプロイ、設定、監視、ポリシー管理など、データプレーン以外のすべての管理機能を提供します。
*   **BOM (Bill Of Materials)**: ソフトウェア開発における依存関係のリストまたは構成要素の宣言であり、特定のコンポーネントが動作するために必要な他のコンポーネントとそのバージョンを定義します。ここでは、Google Cloudが使用する内部ライブラリ群のバージョンを指します。
*   **protobuf (Protocol Buffers)**: Googleが開発した、構造化されたデータをシリアライズするための言語に依存しない、プラットフォームに依存しない、拡張可能なメカニズムです。
*   **gRPC**: Googleが開発した、高性能なオープンソースの汎用RPC (Remote Procedure Call) フレームワークです。
*   **Guava**: Googleが提供するJavaのオープンソースライブラリコレクションで、Javaのコア機能の拡張とユーティリティを提供します。
*   **LLMTokenQuota / PromptTokenLimit policies**: 大規模言語モデル (LLM) 関連のAPI呼び出しにおいて、トークンの消費量やプロンプトの長さを制限・制御するためにApigeeで使用されるポリシーです。
*   **API Product**: ApigeeでAPIをバンドルし、開発者向けに公開するための論理的なグループです。
*   **OAuthV2 policy**: ApigeeでOAuth 2.0認証フローを実装し、APIへのアクセスを制御するためのポリシーです。
*   **apigee-ca certificate**: Apigee内部のコンポーネント間のセキュアな通信や認証に使用される、内部認証局 (CA) の証明書です。

---

## Security
原文:
| Bug ID | Description |
|---|---|
| **535928300** | **Security fix for Apigee.** Fixed a security issue in JWT refresh token revocation handling. |
| **539515020** | **Security fix for Apigee.** Fixed a security issue in the MessageValidation policy. |
| **535928530** | **Security fix for Apigee.** Fixed a security issue in the OAuthV2 policy. |
| **535683286** | **Security fix for Apigee.** Fixed a security issue in HTTP target interim-response handling. |
| **N/A** | **Security fix for Apigee infrastructure.** |

説明:
以下のセキュリティ脆弱性が修正されました。
*   **JWTリフレッシュトークン失効処理のセキュリティ修正 (535928300)**: JWTリフレッシュトークンの失効処理に関するセキュリティ問題が修正されました。
*   **MessageValidationポリシーのセキュリティ修正 (539515020)**: MessageValidationポリシーに関するセキュリティ問題が修正されました。
*   **OAuthV2ポリシーのセキュリティ修正 (535928530)**: OAuthV2ポリシーに関するセキュリティ問題が修正されました。
*   **HTTPターゲット暫定レスポンス処理のセキュリティ修正 (535683286)**: HTTPターゲットへのリクエストにおける暫定レスポンス処理に関するセキュリティ問題が修正されました。
*   **Apigeeインフラストラクチャのセキュリティ修正 (N/A)**: Apigeeインフラストラクチャに関する一般的なセキュリティ問題が修正されました。

影響有無:
**影響あり**:
*   これらのセキュリティ修正は、Apigee環境の全体的なセキュリティ体制を強化し、潜在的な脆弱性からの保護を向上させます。これはポジティブな影響です。
**影響なし**:
*   これらの修正は、セキュリティ脆弱性の改善を目的としているため、既存のAPIの機能や動作に直接的な変更をもたらすものではありません。

対処方法:
1.  これらのセキュリティ修正は、Apigeeのアップデートプロセス中に自動的に適用されるため、お客様側で特段の対処は不要です。
2.  今回のアップデートにより、Apigee環境のセキュリティが向上したことを認識してください。

用語説明:
*   **JWT (JSON Web Token)**: クライアントとサーバー間で情報を安全に伝達するためのコンパクトでURLセーフな方法です。主に認証と認可に使用されます。
*   **Refresh Token (リフレッシュトークン)**: アクセストークンが有効期限切れになった際に、新しいアクセストークンを取得するために使用される、有効期限の長いトークンです。
*   **MessageValidation policy**: ApigeeでXMLまたはJSONメッセージのスキーマ検証を行い、メッセージの形式や内容が期待通りであることを確認するためのポリシーです。
*   **OAuthV2 policy**: ApigeeでOAuth 2.0認証フローを実装するためのポリシーです。アクセストークンの検証、生成、リフレッシュなどを制御します。
*   **HTTP target interim-response handling**: ApigeeがバックエンドのHTTPターゲットサービスとの通信において、HTTP/1.1の1xxシリーズ（例: 100 Continue）のような暫定的なレスポンスをどのように処理するかに関する機能です。