
# Title: July 27, 2026 
Link: https://docs.cloud.google.com/release-notes#July_27_2026<br>
はい、承知いたしました。Google Kubernetes Engineのリリースノートについて、製品への影響調査を実施し、以下の通り回答いたします。

---

# Google Kubernetes Engine

## Fixed

**原文:**
The general availability (GA) stage of mixed-protocol Services of type LoadBalancer fixes errors in traffic routing from stages prior to GA. This feature is in the GA stage in GKE version 1.36.2-gke.1498000 and later.

**説明:**
Kubernetesの`Service`リソースで`type: LoadBalancer`を指定し、かつ複数のプロトコル（例: TCPとUDP）を同時に扱う「mixed-protocol Services of type LoadBalancer」機能が、一般提供（GA）段階になりました。
このGA化に伴い、GA以前のプレビュー段階（Public Previewなど）で発生していたトラフィックルーティングに関するエラーが修正されました。この修正が適用されているのは、GKEバージョン1.36.2-gke.1498000以降です。

**影響有無:**
**影響あり（改善）**

*   もし貴社がGKEクラスタで「mixed-protocol Services of type LoadBalancer」を以前から利用しており、かつクラスタのGKEバージョンが`1.36.2-gke.1498000`未満の場合、本リリースにより、該当サービスにおけるトラフィックルーティングの潜在的なエラーが修正され、安定性が向上します。
*   現在この機能を利用していない場合でも、将来的にこの機能を利用する際に、GA版の安定した動作が期待できます。

**対処方法:**
1.  **GKEバージョンの確認:** 現在ご利用中のGKEクラスタのバージョンが`1.36.2-gke.1498000`以上であるかを確認してください。
    *   `gcloud container clusters describe CLUSTER_NAME --zone ZONE` コマンドで `currentMasterVersion` を確認します。
2.  **Serviceの利用状況確認:** Kubernetesクラスタ内で`type: LoadBalancer`の`Service`リソースにおいて、複数のプロトコルを同時に定義している（`mixed-protocol Services`を利用している）か確認してください。
    *   `kubectl get svc -A -o yaml` でService定義を確認し、`ports`セクションに複数のプロトコル（例: `protocol: TCP`と`protocol: UDP`）が混在しているか確認します。
3.  **バージョンアップの検討:** もし上記1と2の両方に該当し、かつトラフィックルーティングに関する問題に直面していた場合、GKEクラスタを`1.36.2-gke.1498000`以降のバージョンにアップグレードすることを検討してください。これにより、該当の問題が解消される可能性があります。

**用語説明:**
*   **Google Kubernetes Engine (GKE):** Google Cloudが提供するマネージドなKubernetesサービスです。コンテナ化されたアプリケーションのデプロイ、スケーリング、管理を容易にします。
*   **Service of type LoadBalancer:** KubernetesのServiceリソースの一種です。このタイプを指定すると、Kubernetesクラスタ外部からアクセス可能なロードバランサー（Google Cloudの場合、Cloud Load Balancing）が自動的にプロビジョニングされ、クラスタ内のPodsへの外部からのアクセスを可能にします。
*   **Mixed-protocol Services:** 単一のKubernetes Service定義内で、異なるネットワークプロトコル（例: TCP、UDP）のトラフィックを同時に処理できるようにする機能です。
*   **General Availability (GA):** ソフトウェアや機能が完全に開発され、テストされ、本番環境での利用に適していると公式に認められた段階を指します。GA段階の機能は、通常、品質保証とサポートが提供されます。
*   **Traffic Routing:** ネットワーク上でデータパケットが送信元から最終的な宛先へどのように送られるかを決定するプロセスです。ロードバランサーやネットワークデバイスがこのルーティングを担当します。
# Title: July 24, 2026 
Link: https://docs.cloud.google.com/release-notes#July_24_2026<br>
Google Cloud のインフラエンジニアとして、GKE のリリースノートに対する調査結果を以下に報告します。

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
## No channel (deprecated)

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.35.6-gke.1127000 is now the default version for cluster creation.
- The following versions are now available:

- 1.33.13-gke.1269000
- 1.34.9-gke.1610000
- 1.35.6-gke.1638000
- 1.35.6-gke.1641000
- 1.36.2-gke.2064000

- The following node versions are now available:

- 1.30.14-gke.2846000
- 1.31.14-gke.2437000
- 1.32.13-gke.2137000
- 1.33.13-gke.1269000
- 1.34.9-gke.1610000
- 1.35.6-gke.1638000
- 1.35.6-gke.1641000
- 1.36.2-gke.2064000

- The following versions are no longer available:

- 1.35.5-gke.1241004 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.36.0-gke.3712000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:

- 1.32 to 1.33.13-gke.1011000

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:

- 1.33 to 1.33.13-gke.1011000
- 1.35 to 1.35.6-gke.1127000
- 1.36 to 1.36.0-gke.4447000

説明:
GKEクラスタのバージョンが更新されました。新しいGKEクラスタの作成時、および既存クラスタの手動でのコントロールプレーンやノードのアップグレードで、これらのバージョンが利用可能です。
このアナウンスでは、特定のリリースチャンネルに依存しない一般的なGKEバージョン更新情報が含まれています。

*   **新規利用可能バージョン**: GKEコントロールプレーンおよびノードの両方で、バージョン1.33.13-gke.1269000から1.36.2-gke.2064000までの複数の新しいパッチバージョンが利用可能になりました。
*   **新規クラスタのデフォルトバージョン**: 1.35.6-gke.1127000が新しいクラスタ作成時のデフォルトバージョンとなりました。
*   **非推奨バージョン**: 1.35.5-gke.1241004と1.36.0-gke.3712000が非推奨となり、90日以内、またはサポート終了時に削除されます。
*   **自動アップグレードターゲット**: GKEクラスタの自動アップグレードターゲットが更新され、特定のマイナーバージョンから新しいマイナーバージョンへ、または既存のマイナーバージョンの新しいパッチバージョンへのアップグレードが実行される可能性があります。メンテナンス除外期間や非推奨APIの使用などの要因がない場合、これらのターゲットにアップグレードされます。

影響有無:
*   **既存のGKEクラスタ**: 現在利用中のクラスタが非推奨バージョン（1.35.5-gke.1241004または1.36.0-gke.3712000）を使用している場合、90日以内に強制削除されるため、早急なアップグレードが必要です。自動アップグレードが有効な場合、設定されているメンテナンスウィンドウに基づいて、新しいターゲットバージョンへのアップグレードが行われる可能性があります。
*   **新規GKEクラスタ**: 新規に作成されるクラスタは、デフォルトでバージョン1.35.6-gke.1127000でプロビジョニングされます。
*   **Google Cloud Composer2 (Composer 2.7.1, Airflow 2.7.3)**:
    *   Composer 2.7.1は、GKEバージョン1.25, 1.26, 1.27, 1.28をサポートしています。今回のリリースノートに記載されているGKEバージョン（1.30以上）は、現在のComposer 2.7.1のサポート範囲外です。
    *   したがって、現在のComposer 2.7.1環境が、これらの新規提供または非推奨となったGKEバージョンに直接影響を受けることはありません。Composerの基盤となるGKEバージョンはComposerサービスによって管理されており、ユーザーが直接GKEバージョンを指定・変更することはできません。
    *   ただし、将来的にComposerがこれらの新しいGKEバージョンをサポートし始める際には、これらの変更が適用されます。

対処方法:
*   **既存のGKEクラスタ**:
    *   `gcloud container clusters list --uri` コマンドなどでクラスタの現在のバージョンを確認し、非推奨バージョンを使用している場合は速やかにアップグレード計画を立ててください。
    *   自動アップグレード設定を確認し、メンテナンスウィンドウや除外期間が適切に設定されているか検証してください。
    *   アップグレード前に、新しいGKEバージョンのリリースノートとKubernetesチェンジログを確認し、アプリケーションとの互換性を評価してください。
*   **Google Cloud Composer2**:
    *   現時点での直接的な対処は不要ですが、Composerのバージョンアップグレードを検討する際は、新しいComposerバージョンがサポートするGKEバージョンと、そのGKEバージョンにおける非推奨APIや変更点を事前に確認してください。
    *   Composerのリリースノートを定期的に確認し、GKEバージョンの更新に関するアナウンスに注意してください。

用語説明:
*   **コントロールプレーン (Control Plane)**: Kubernetesクラスタの管理機能を提供するコンポーネント群（APIサーバー、スケジューラ、コントローラマネージャ、etcdなど）。
*   **ノード (Node)**: Kubernetesクラスタ内でコンテナ化されたワークロードを実行する仮想マシンまたは物理マシン。
*   **自動アップグレードターゲット (Auto-upgrade Targets)**: GKEクラスタが自動的にアップグレードされる際の目標バージョン。
*   **メンテナンス除外期間 (Maintenance Exclusions)**: GKEクラスタの自動メンテナンス（アップグレードなど）が実行されないように指定する期間。
*   **非推奨 (Deprecated)**: 将来的にサポートが終了し、削除される予定の機能やバージョン。

---

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


1.32.13-gke.2137000
cos-117-18613-675-2
cos-117-18613-675-2 release notes


1.34.9-gke.1610000
cos-125-19216-532-3
cos-125-19216-532-3 release notes


1.36.2-gke.2064000
cos-129-19506-299-3
cos-129-19506-299-3 release notes

説明:
本リリースに含まれる新しいGKEバージョンは、更新されたContainer-Optimized OS (COS) イメージを使用しています。これらの更新されたイメージには、以前のGKEリリース以降にリリースされた全てのCOSバージョンからの累積的なセキュリティ修正が含まれています。詳細な脆弱性情報については、各COSイメージのリリースノートを参照するように案内されています。

影響有無:
*   **既存のGKEクラスタ**: GKEクラスタをこれらの新しいバージョンにアップグレードすることで、基盤となるOSレベルのセキュリティ脆弱性修正が適用され、クラスタ全体のセキュリティ体制が向上します。これはポジティブな影響です。
*   **Google Cloud Composer2 (Composer 2.7.1, Airflow 2.7.3)**:
    *   Composer環境も基盤としてGKEを使用し、そのGKEクラスタはCOSイメージを使用しています。Composerのバージョンアップグレードにより、Composerが利用するGKEバージョンが更新されると、それに伴い基盤OSのセキュリティ修正も適用され、環境全体のセキュリティが強化されます。
    *   現在のComposer 2.7.1は、今回のリリースノートに記載されているGKEバージョン（1.30以上）の範囲外であるため、即座にこれらのセキュリティ修正が適用されるわけではありません。しかし、セキュリティの向上は常に推奨されるため、将来的なGKEまたはComposerのアップグレード時にはこの恩恵を受けられます。

対処方法:
*   **既存のGKEクラスタ**: GKEクラスタのバージョンアップグレードを計画し、セキュリティ修正を適用することを推奨します。
*   **Google Cloud Composer2**: Composerのバージョンを最新に保つことで、Composerサービスが管理するGKEバージョンも最新化され、基盤OSのセキュリティ修正が適用されます。Composerのバージョンアップグレードロードマップに合わせて、セキュリティの向上を継続的に行うことを検討してください。

用語説明:
*   **Container-Optimized OS (COS)**: Google CloudでKubernetesクラスタのノードとして推奨される、コンテナ実行に最適化されたオペレーティングシステム。

---

## Change

原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- The following versions are now available in the Stable channel:

- 1.33.12-gke.1270000
- 1.34.9-gke.1065000

説明:
GKE Stableチャンネルで新しいバージョンが利用可能になりました。これらのバージョンは、既存のクラスタの手動アップグレードや新規クラスタの作成で選択できるようになります。

影響有無:
*   **既存のGKEクラスタ**: Stableチャンネルを使用しているクラスタの場合、これらの新しいバージョンへのアップグレードが可能です。Stableチャンネルは、より広範なユーザーベースによってテストされた、安定性の高いバージョンを提供します。
*   **Google Cloud Composer2 (Composer 2.7.1, Airflow 2.7.3)**:
    *   Composer 2.7.1はGKEバージョン1.25, 1.26, 1.27, 1.28をサポートしており、今回Stableチャンネルで利用可能になったバージョン（1.33.12, 1.34.9）はサポート範囲外です。
    *   Composer 2.xは通常、GKEのRegularチャンネルを使用することが多いため、Stableチャンネルの更新が直接Composer環境に影響を与える可能性は低いと考えられます。

対処方法:
*   **既存のGKEクラスタ**: Stableチャンネルを使用している場合、またはStableチャンネルへの移行を検討している場合は、これらのバージョンへのアップグレードを評価してください。
*   **Google Cloud Composer2**: 特段の対処は不要です。

用語説明:
*   **Stableチャンネル (Stable channel)**: GKEのリリースチャンネルの一つで、本番環境での利用に適した、最も安定性が高く、十分にテストされたバージョンを提供します。

---

## Change

原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.35.6-gke.1127000 is now the default version for cluster creation in the Regular channel.
- The following versions are now available in the Regular channel:

- 1.33.13-gke.1101000
- 1.34.9-gke.1287000
- 1.35.6-gke.1250000
- 1.36.0-gke.4681000
- 1.36.2-gke.1346000

- The following versions are no longer available in the Regular channel:

- 1.33.12-gke.1270000
- 1.34.9-gke.1065000
- 1.35.6-gke.1049000
- 1.36.0-gke.3712000 is deprecated in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:

- 1.32 to 1.33.13-gke.1011000
- 1.33 to 1.34.9-gke.1131000
- 1.34 to 1.35.6-gke.1127000

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:

- 1.33 to 1.33.13-gke.1011000
- 1.34 to 1.34.9-gke.1131000
- 1.35 to 1.35.6-gke.1127000
- 1.36 to 1.36.0-gke.4447000

説明:
GKE Regularチャンネルでクラスタバージョンが更新されました。

*   **新規利用可能バージョン**: 1.33.13-gke.1101000から1.36.2-gke.1346000までの複数の新しいパッチバージョンがRegularチャンネルで利用可能になりました。
*   **新規クラスタのデフォルトバージョン**: 1.35.6-gke.1127000がRegularチャンネルにおける新しいクラスタ作成時のデフォルトバージョンとなりました。
*   **非推奨バージョン**: 1.33.12-gke.1270000、1.34.9-gke.1065000、1.35.6-gke.1049000、および1.36.0-gke.3712000がRegularチャンネルで非推奨となり、後者は90日以内、またはサポート終了時に削除されます。
*   **自動アップグレードターゲット**: Regularチャンネルの自動アップグレードターゲットが更新され、特定のマイナーバージョンから新しいマイナーバージョンへ、または既存のマイナーバージョンの新しいパッチバージョンへのアップグレードが実行される可能性があります。

影響有無:
*   **既存のGKEクラスタ**: Regularチャンネルを使用しているクラスタの場合、非推奨バージョンに該当するバージョンを使用している場合は90日以内に強制削除されるため、早急なアップグレードが必要です。自動アップグレードが有効な場合、設定されたメンテナンスウィンドウに従って新しいターゲットバージョンにアップグレードされる可能性があります。
*   **Google Cloud Composer2 (Composer 2.7.1, Airflow 2.7.3)**:
    *   Composer 2.7.1はGKEバージョン1.25, 1.26, 1.27, 1.28をサポートしており、今回Regularチャンネルで利用可能/非推奨となったバージョン（1.33以上）はサポート範囲外です。
    *   Composer 2.xは一般的にRegularチャンネルを使用しますが、現在のComposer 2.7.1がサポートするGKEバージョンと、このリリースノートに記載されているGKEバージョンとの間に乖離があるため、直接的な影響はありません。ComposerサービスがGKEバージョンを管理するため、ユーザーが直接アップグレードを行う必要もありません。ただし、将来的にComposerがこれらの新しいGKEバージョンをサポートし始めた際には、これらの変更が適用されます。

対処方法:
*   **既存のGKEクラスタ**:
    *   Regularチャンネルを使用しているクラスタで非推奨バージョンが稼働している場合は、速やかにアップグレードを計画してください。
    *   自動アップグレードの動作を確認し、アプリケーションへの影響を最小限に抑えるため、メンテナンスウィンドウや除外期間を適切に設定してください。
*   **Google Cloud Composer2**: 特段の対処は不要ですが、Composerのバージョンアップグレード計画時に、GKEバージョンの互換性と非推奨APIの影響を確認してください。

用語説明:
*   **Regularチャンネル (Regular channel)**: GKEのリリースチャンネルの一つで、最新の安定バージョンと機能が提供されます。ほとんどのユーザーに適しています。

---

## Change

原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.36.2-gke.1498000 is now the default version for cluster creation in the Rapid channel.
- The following versions are now available in the Rapid channel:

- 1.33.13-gke.1269000
- 1.34.9-gke.1610000
- 1.35.6-gke.1638000
- 1.35.6-gke.1641000
- 1.36.2-gke.2064000

- The following versions are no longer available in the Rapid channel:

- 1.33.13-gke.1101000
- 1.34.9-gke.1287000
- 1.35.6-gke.1250000
- 1.36.0-gke.4681000
- 1.36.2-gke.1346000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:

- 1.32 to 1.33.13-gke.1109000
- 1.33 to 1.34.9-gke.1322000
- 1.34 to 1.35.6-gke.1258000
- 1.35 to 1.36.2-gke.1498000

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:

- 1.33 to 1.33.13-gke.1109000
- 1.34 to 1.34.9-gke.1322000
- 1.35 to 1.35.6-gke.1258000