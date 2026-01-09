
# Title: January 07, 2026 
Link: https://docs.cloud.google.com/release-notes#January_07_2026<br>
はい、承知いたしました。Google Kubernetes Engine (GKE) に関するリリースノートを分析し、ご指定の形式で回答いたします。

---

# Google Kubernetes Engine
## Change
原文: GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.
[GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)
説明: GKEクラスタのバージョンが更新され、新しいバージョンが利用可能になりました。これらの新しいバージョンは、新規GKEクラスタの作成時や、既存クラスタのコントロールプレーンおよびノードの手動アップグレード時に選択できます。
影響有無: 中程度。
理由: 既存クラスタの自動アップグレードが有効な場合、メンテナンスウィンドウ期間内に新しいバージョンへのアップグレードが自動的に行われる可能性があります。新しいクラスタを作成する際は、デフォルトでこの新しいバージョンが適用されることがあります。通常、パッチバージョンアップグレードは互換性を保ちますが、アプリケーションによっては影響が出る可能性も考慮し、リリースノートの変更詳細を確認することが推奨されます。
対処方法:
*   既存クラスタのGKEバージョン、リリースチャネル、自動アップグレード設定を確認してください。
*   手動アップグレードを計画している場合、提供されているGKEバージョンニングとアップグレードのドキュメントを参照し、計画的なアップグレードを実施してください。
用語説明:
*   **GKEバージョン**: Google Kubernetes Engineのバージョンは、Kubernetes本体のバージョンにGKE固有のパッチバージョンが付与された形式（例: 1.35.0-gke.1403000）で表されます。
*   **コントロールプレーン**: Kubernetesクラスタの管理層を指します。APIサーバ、スケジューラ、コントローラマネージャ、etcdなどが含まれ、クラスタ全体の状態管理と操作を行います。
*   **ノード**: ワークロード（Pod）が実際に実行される仮想マシンまたは物理マシンのことです。

---

# Google Kubernetes Engine
## Security
原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release. To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the **Security** release notes for that image. The following table includes links to the release notes for each updated Container-Optimized OS image:
GKE version
Container-Optimized OS version
Details
1.35.0-gke.1403000
cos-125-19216-104-45
cos-125-19216-104-45 release notes
[cos-125-19216-104-45 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m125#cos-125-19216-104-45_)
説明: 今回のGKEリリースに含まれる新しいバージョンでは、更新されたContainer-Optimized OS (COS) イメージが使用されています。これらのイメージには、前回のGKEリリース以降に公開されたすべてのCOSバージョンからの累積的なセキュリティ修正が含まれています。詳細な脆弱性情報は、各COSイメージのリリースノートで確認できます。
影響有無: なし（ポジティブな影響）。
理由: クラスタノードのOSレベルのセキュリティ脆弱性が修正され、セキュリティ体制が強化されます。これは通常、アプリケーションへの直接的な非互換性影響を伴いません。
対処方法: クラスタのセキュリティを最新の状態に保つため、GKEクラスタを最新バージョンにアップグレードすることを推奨します。自動アップグレード設定が有効になっていることを確認してください。
用語説明:
*   **Container-Optimized OS (COS)**: Googleが開発した、コンテナの実行に特化したChrome OSベースのLinuxディストリビューションです。セキュリティ、信頼性、コンテナ実行時のパフォーマンスが最適化されています。

---

# Google Kubernetes Engine
## Change
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.33.5-gke.2019000 is now the default version for cluster creation in the Extended channel.
- The following versions are now available in the Extended channel: ...
- The following versions are no longer available in the Extended channel: ...
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: ...
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades: ...
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades: ...
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)
説明: Extendedリリースチャネルにおいて、GKEクラスタの新しいデフォルトバージョン（1.33.5-gke.2019000）が設定され、新しい利用可能バージョンが追加され、同時にいくつかの古いバージョンは利用不可となりました。このチャネル内のクラスタには、コントロールプレーンとノードの新しい自動アップグレードターゲットが設定されました。バージョンは段階的にロールアウトされるため、すぐに全てのゾーンで利用可能ではない場合があります。
影響有無: 中程度。
理由:
*   **新規クラスタ作成**: Extendedチャネルでクラスタを新規作成する場合、デフォルトで新しいバージョンが適用されます。
*   **既存クラスタ**: 自動アップグレードが有効な場合、クラスタはメンテナンスウィンドウ中に新しいターゲットバージョンに自動的にアップグレードされる可能性があります。特にマイナーバージョンアップグレードの場合、APIの非互換性や機能変更によりアプリケーションに影響が出る可能性があります。利用不可となったバージョンを使用している場合、手動でそのバージョンに固定し続けることはできなくなります。
対処方法:
*   Extendedチャネルを利用している場合、既存クラスタのバージョンと、自動アップグレードが有効であるかを確認してください。
*   自動アップグレードのターゲットバージョン（特にマイナーバージョンアップグレード）に含まれる変更点や非推奨API（Deprecated APIs）がないか、Kubernetesの変更履歴（リンク参照）を確認し、アプリケーションへの影響を評価してください。
*   アップグレードはメンテナンスウィンドウまたはメンテナンス除外期間を考慮して行われるため、これらの設定が適切であることを確認してください。
用語説明:
*   **リリースチャネル (Release Channel)**: GKEクラスタのバージョンライフサイクルを管理するための仕組み。Rapid, Regular, Stable, Extendedなどのチャネルがあり、それぞれバージョン提供の速度や安定性、サポート期間が異なります。Extendedチャネルは長期サポートを提供します。
*   **自動アップグレードターゲット**: GKEが自動アップグレードの際に目指す目標バージョンです。メンテナンス除外設定や非推奨APIの使用状況によっては、アップグレードが妨げられる場合があります。
*   **メンテナンス除外 (Maintenance Exclusions)**: 特定の期間、GKEの自動アップグレードやメンテナンス活動が行われないように設定できる機能です。

---

# Google Kubernetes Engine
## Change
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.33.5-gke.2019000 is now the default version for cluster creation.
- The following versions are now available: ...
- The following node versions are now available: ...
- The following versions are no longer available: ...
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: ...
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades: ...
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades: ...
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)
説明: 新規クラスタ作成時のデフォルトバージョンが1.33.5-gke.2019000に変更され、新しいGKEバージョンとノードバージョンが利用可能になりました。同時に、一部の古いバージョンは利用不可となっています。クラスタの自動アップグレードターゲットも更新され、コントロールプレーンとノードが新しいバージョンにアップグレードされる可能性があります。これらの変更は段階的にロールアウトされます。
影響有無: 中程度。
理由:
*   **新規クラスタ作成**: 新しいデフォルトバージョンが適用されます。
*   **既存クラスタ**: 自動アップグレードが有効な場合、クラスタはメンテナンスウィンドウ中に新しいターゲットバージョンに自動的にアップグレードされる可能性があります。利用不可となったバージョンを使用中のクラスタは、将来的にアップグレードが必須となります。
対処方法: 上記「Extended Channel」の変更点と同様に、既存クラスタのバージョン、リリースチャネル、自動アップグレード設定を確認し、アップグレードによる影響（特にマイナーバージョンアップグレードに伴うAPIの非互換性など）を評価してください。
用語説明: 上記「Extended Channel」の用語説明と同様です。

---

# Google Kubernetes Engine
## Change
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.35.0-gke.1340000 is now the default version for cluster creation in the Rapid channel.
- The following versions are now available in the Rapid channel: ...
- The following versions are no longer available in the Rapid channel: ...
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: ...
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades: ...
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades: ...
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)
説明: Rapidリリースチャネルにおいて、GKEクラスタの新しいデフォルトバージョン（1.35.0-gke.1340000）が設定され、新しい利用可能バージョンが追加され、同時にいくつかの古いバージョンは利用不可となりました。このチャネル内のクラスタには、コントロールプレーンとノードの新しい自動アップグレードターゲットが設定されました。バージョンは段階的にロールアウトされるため、すぐに全てのゾーンで利用可能ではない場合があります。
影響有無: 中程度。
理由:
*   **新規クラスタ作成**: Rapidチャネルでクラスタを新規作成する場合、デフォルトで新しいバージョンが適用されます。
*   **既存クラスタ**: Rapidチャネルは最も頻繁にバージョンが更新されるため、自動アップグレードが有効な場合、迅速に新しいバージョンにアップグレードされる可能性が高く、マイナーバージョンアップグレードによるAPIの非互換性や機能変更の影響を早期に受ける可能性があります。利用不可となったバージョンを使用している場合、手動でそのバージョンに固定し続けることはできなくなります。
対処方法:
*   Rapidチャネルを利用している場合、GKEのバージョン更新頻度が高いため、アプリケーションの互換性テストを迅速に行う体制を確立することが重要です。
*   自動アップグレードのターゲットバージョンに含まれる変更点や非推奨APIがないか、Kubernetesの変更履歴を確認し、アプリケーションへの影響を評価してください。
*   アップグレードはメンテナンスウィンドウまたはメンテナンス除外期間を考慮して行われるため、これらの設定が適切であることを確認してください。
用語説明:
*   **Rapidチャネル**: GKEリリースチャネルの一つで、最新の機能やセキュリティアップデートが最も早く提供されるチャネルです。新機能の検証や開発環境に適していますが、他のチャネルに比べてアップグレード頻度が高く、サポート期間が短いです。

---

# Google Kubernetes Engine
## Change
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.33.5-gke.2019000 is now the default version for cluster creation in the Regular channel.
- The following versions are now available in the Regular channel: ...
- The following versions are no longer available in the Regular channel: ...
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: ...
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades: ...
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades: ...
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)
説明: Regularリリースチャネルにおいて、GKEクラスタの新しいデフォルトバージョン（1.33.5-gke.2019000）が設定され、新しい利用可能バージョンが追加され、同時にいくつかの古いバージョンは利用不可となりました。このチャネル内のクラスタには、コントロールプレーンとノードの新しい自動アップグレードターゲットが設定されました。バージョンは段階的にロールアウトされるため、すぐに全てのゾーンで利用可能ではない場合があります。
影響有無: 中程度。
理由:
*   **新規クラスタ作成**: Regularチャネルでクラスタを新規作成する場合、デフォルトで新しいバージョンが適用されます。
*   **既存クラスタ**: 自動アップグレードが有効な場合、クラスタはメンテナンスウィンドウ中に新しいターゲットバージョンに自動的にアップグレードされる可能性があります。マイナーバージョンアップグレードの場合、APIの非互換性や機能変更によりアプリケーションに影響が出る可能性があります。利用不可となったバージョンを使用している場合、手動でそのバージョンに固定し続けることはできなくなります。
対処方法:
*   Regularチャネルを利用している場合、既存クラスタのバージョンと、自動アップグレードが有効であるかを確認してください。
*   自動アップグレードのターゲットバージョンに含まれる変更点や非推奨APIがないか、Kubernetesの変更履歴を確認し、アプリケーションへの影響を評価してください。
*   アップグレードはメンテナンスウィンドウまたはメンテナンス除外期間を考慮して行われるため、これらの設定が適切であることを確認してください。
用語説明:
*   **Regularチャネル**: GKEリリースチャネルの一つで、十分なテストが行われた後に新しい機能やアップデートが提供されるバランスの取れたチャネルです。本番環境で一般的に推奨されます。

---

# Google Kubernetes Engine
## Change
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.33.5-gke.1308000 is now the default version for cluster creation in the Stable channel.
- The following versions are now available in the Stable channel: ...
- The following versions are no longer available in the Stable channel: ...
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: ...
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades: ...
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades: ...
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)
説明: Stableリリースチャネルにおいて、GKEクラスタの新しいデフォルトバージョン（1.33.5-gke.1308000）が設定され、新しい利用可能バージョンが追加され、同時にいくつかの古いバージョンは利用不可となりました。このチャネル内のクラスタには、コントロールプレーンとノードの新しい自動アップグレードターゲットが設定されました。バージョンは段階的にロールアウトされるため、すぐに全てのゾーンで利用可能ではない場合があります。
影響有無: 中程度。
理由:
*   **新規クラスタ作成**: Stableチャネルでクラスタを新規作成する場合、デフォルトで新しいバージョンが適用されます。
*   **既存クラスタ**: 自動アップグレードが有効な場合、クラスタはメンテナンスウィンドウ中に新しいターゲットバージョンに自動的にアップグレードされる可能性があります。Stableチャネルは最も安定性が高く、アップグレード頻度は低いですが、マイナーバージョンアップグレードの場合、APIの非互換性や機能変更によりアプリケーションに影響が出る可能性があります。利用不可となったバージョンを使用している場合、手動でそのバージョンに固定し続けることはできなくなります。
対処方法:
*   Stableチャネルを利用している場合、既存クラスタのバージョンと、自動アップグレードが有効であるかを確認してください。
*   自動アップグレードのターゲットバージョンに含まれる変更点や非推奨APIがないか、Kubernetesの変更履歴を確認し、アプリケーションへの影響を評価してください。
*   アップグレードはメンテナンスウィンドウまたはメンテナンス除外期間を考慮して行われるため、これらの設定が適切であることを確認してください。
用語説明:
*   **Stableチャネル**: GKEリリースチャネルの一つで、最も安定性が高く、長期サポートが提供されるチャネルです。重要な本番環境での利用に推奨されます。

---
# Title: January 06, 2026 
Link: https://docs.cloud.google.com/release-notes#January_06_2026<br>
はい、承知いたしました。Google Cloudのリリースノートを元に、GKEに関する変更点について、影響調査と対応方針を回答します。

---

# Google Kubernetes Engine

## Fixed

原文:
A fix is available for the December 16, 2025 issue in which Autopilot nodes enter into a state where new system Pods and user Pods are unable to run due to NRI RunPodSandbox failures. For more details, including instructions on how to confirm if you're affected by this, see Pods unable to run on a Node due to NRI RunPodSandbox failed.
The fix is available with GKE version 1.34.1-gke.3899000 and later.

説明：
本リリースは、Google Kubernetes Engine (GKE) のAutopilotモードで発生していた既知の問題に対する修正提供のアナウンスです。この問題は、Autopilotクラスタのノードにおいて、NRI RunPodSandbox処理が失敗することで、新しいシステムPodやユーザーPodが正常に起動できなくなるというものです。この修正は、GKEバージョン1.34.1-gke.3899000以降で利用可能です。影響を受けているかどうかの確認方法と詳細な情報については、提供されているトラブルシューティングドキュメント（[Pods unable to run on a Node due to NRI RunPodSandbox failed](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/autopilot-clusters#nri-runpodsandbox-error)）を参照してください。

影響有無：
**影響あり（潜在的）**

理由：
*   GKE Autopilotクラスタを利用している場合、この問題に遭遇する可能性があります。ただし、修正が提供されたことで、適切なGKEバージョンに更新されていれば影響を回避できます。
*   もし現在、AutopilotクラスタでPodが起動できない問題に直面している場合は、本件の修正が直接的に関連している可能性があります。

対処方法：
1.  **GKEバージョンの確認:** 運用中のGKE Autopilotクラスタが、GKEバージョン1.34.1-gke.3899000以降にアップデートされていることを確認してください。Autopilotクラスタは通常、自動的にアップデートされますが、メンテナンスウィンドウの設定によっては時間がかかる場合があります。
2.  **問題発生時の対応:** もし現在、Autopilotクラスタで新規Podが起動できない、またはPodが`Pending`状態のままになっているといった問題が発生している場合は、Google Cloudのドキュメント「[Pods unable to run on a Node due to NRI RunPodSandbox failed](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/autopilot-clusters#nri-runpodsandbox-error)」を参照し、自身がこの問題の影響を受けているか確認し、記載された手順に従って対処してください。

用語説明：
*   **GKE Autopilot:** Google Kubernetes Engineの運用モードの一つで、クラスタのノードや基盤インフラの管理をGoogleが完全に自動化します。ユーザーはワークロードのデプロイに集中できます。
*   **NRI (Node Runtime Interface):** Kubernetesのコンテナランタイム（例えばcontainerd）がノード上でPodのライフサイクルを管理するために使用するインターフェースの一部です。
*   **RunPodSandbox:** NRI/CRI (Container Runtime Interface) のAPI呼び出しの一つで、Podを実行するための隔離された環境（サンドボックス、通常はコンテナランタイムが管理するネームスペースやcgroupのセット）を作成する操作を指します。この操作が失敗すると、そのサンドボックス内でコンテナを起動できず、結果としてPodが起動できません。
*   **Pod:** Kubernetesにおけるデプロイの最小単位です。1つまたは複数のコンテナ、ストレージ、特定のネットワーク設定、およびコンテナの実行方法に関する仕様が含まれます。
*   **System Pods:** Kubernetesクラスタ自身の動作に必要なコンポーネント（例: kube-proxy, CoreDNS）を実行するPodです。
*   **User Pods:** ユーザーがデプロイするアプリケーションやサービスを実行するPodです。

---
# Title: January 05, 2026 
Link: https://docs.cloud.google.com/release-notes#January_05_2026<br>
Google Cloud インフラエンジニアとして、ご提示いただいたリリースノートについて、製品への影響有無を調査し、以下の通りご回答いたします。

---

# Google Kubernetes Engine

## Change
### GKE cluster versions have been updated.
原文: GKE cluster versions have been updated. New versions available for upgrades and new clusters. The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.
説明：GKEクラスタの新しいバージョンがリリースされ、アップグレードおよび新規クラスタ作成で利用可能になりました。これらのバージョンは、既存クラスタのコントロールプレーンおよびノードの手動アップグレードにも利用できます。
影響有無：**影響あり**。
新しいバージョンが利用可能になったことで、新規クラスタの作成時や既存クラスタの手動アップグレード時に選択肢が増えます。特に、Google Cloud Composer 2 はGKEを基盤としているため、Composer環境のGKEバージョンも将来的にこれらの新しいバージョンにアップグレードされる可能性があります。これにより、基盤インフラストラクチャの安定性やパフォーマンス、セキュリティが向上する可能性があります。
対処方法：
*   現在のGKEクラスタのバージョンと、利用しているリリースチャネルを確認してください。
*   既存クラスタのアップグレード計画を検討する際、これらの新しいバージョンを考慮に入れてください。
*   Google Cloud Composer 2をご利用の場合、Composerのドキュメントを参照し、基盤GKEバージョンの管理方法と自動アップグレードのスケジュールを確認してください。GKEバージョンアップグレードがComposerワークロードに影響を与えないか、計画的なテストを実施することを推奨します。

## Security
### This release includes new GKE versions that use updated Container-Optimized OS images.
原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release. To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the Security release notes for that image. GKE version 1.35.0-gke.1340000 Container-Optimized OS version cos-125-19216-104-45.
説明：今回のリリースに含まれるGKEの新しいバージョンには、セキュリティ修正が適用されたContainer-Optimized OS (COS) イメージが使用されています。これらのイメージには、前回のGKEリリース以降に公開されたすべてのCOSバージョンからの累積的なセキュリティ修正が含まれています。特に、GKE 1.35.0-gke.1340000ではcos-125-19216-104-45が採用されています。
影響有無：**間接的に影響あり**。
直接的な変更は発生しませんが、セキュリティ脆弱性が修正された最新のCOSイメージが提供されるため、クラスタのセキュリティ体制を強化する機会が得られます。Google Cloud Composer 2の基盤GKEバージョンがアップグレードされる際、これらのセキュリティ修正が適用されます。
対処方法：
*   GKEクラスタのアップグレードを検討する際、これらのセキュリティ修正が含まれる最新バージョンを選択することで、セキュリティ体制を強化できます。
*   Google Cloud Composer 2をご利用の場合、Composerの自動アップグレードポリシーに従って基盤GKEバージョンがアップグレードされることを確認してください。

## Change
### The following versions are now available in the Extended channel:
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. The following versions are now available in the Extended channel: 1.28.15-gke.3285000, 1.29.15-gke.2617000, 1.30.14-gke.1861000.
説明：Extendedリリースチャネルで、GKEバージョン1.28.15-gke.3285000、1.29.15-gke.2617000、1.30.14-gke.1861000が利用可能になりました。リリースノート公開時点でロールアウトが進行中であり、すべてのGoogle Cloudゾーンで利用可能になるまで数日かかる場合があります。
影響有無：**影響あり**。
Extendedチャネルを利用しているGKEクラスタは、これらのバージョンへのアップグレードが推奨または自動的に行われる可能性があります。Google Cloud Composer 2は通常RapidまたはRegularチャネルを使用することが多いため、直接的な影響は低いですが、Composer環境がExtendedチャネルを利用するように構成されている場合は影響を受けます。
対処方法：
*   Extendedチャネルを利用しているGKEクラスタの場合、これらのバージョンの変更履歴を確認し、アプリケーションへの影響を評価してください。
*   計画的なアップグレードを検討し、メンテナンスウィンドウ内で実施してください。

## Change
### The following versions are now available: (Control Plane & Node versions)
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. The following versions are now available: 1.31.14-gke.1166000, 1.32.9-gke.1728000, 1.33.5-gke.2100000, 1.34.1-gke.3947000. The following node versions are now available: 1.28.15-gke.3285000, 1.29.15-gke.2617000, 1.30.14-gke.1861000, 1.31.14-gke.1166000, 1.32.9-gke.1728000, 1.33.5-gke.2100000, 1.34.1-gke.3947000.
説明：新しいGKEクラスタバージョン（コントロールプレーン）1.31.14-gke.1166000から1.34.1-gke.3947000、および新しいノードバージョン1.28.15-gke.3285000から1.34.1-gke.3947000が利用可能になりました。リリースノート公開時点でロールアウトが進行中であり、すべてのGoogle Cloudゾーンで利用可能になるまで数日かかる場合があります。
影響有無：**影響なし（直接的）/影響あり（間接的）**。
これらのバージョンが利用可能になっただけであり、既存クラスタが自動的にアップグレードされるわけではありません。しかし、新規クラスタの作成時や手動アップグレード時にはこれらのバージョンが選択肢として追加されます。Google Cloud Composer 2の基盤GKEバージョンがこれらの範囲に含まれる場合、将来的に自動アップグレードの対象となる可能性があります。
対処方法：
*   新規GKEクラスタの作成や既存クラスタのアップグレードを計画する際に、これらの新しいバージョンを検討してください。
*   Kubernetesのバージョン間の非互換性がないか、それぞれのCHANGELOGを確認し、アプリケーションへの影響を評価してください。

## Change
### The following versions are now available in the Rapid channel:
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. The following versions are now available in the Rapid channel: 1.31.14-gke.1166000, 1.32.9-gke.1728000, 1.33.5-gke.2100000, 1.34.1-gke.3947000, 1.35.0-gke.1340000.
説明：Rapidリリースチャネルで、GKEバージョン1.31.14-gke.1166000から最新の1.35.0-gke.1340000までのバージョンが利用可能になりました。リリースノート公開時点でロールアウトが進行中であり、すべてのGoogle Cloudゾーンで利用可能になるまで数日かかる場合があります。
影響有無：**影響あり**。
Rapidチャネルを利用しているGKEクラスタは、これらの新しいバージョンへの自動アップグレードの対象となります。特に1.35.0は最新のマイナーバージョンであり、重要な変更が含まれる可能性があります。Google Cloud Composer 2は通常RapidまたはRegularチャネルを利用するため、Composer環境の基盤GKEバージョンがこれらのバージョンに自動アップグレードされる可能性が高いです。
対処方法：
*   Rapidチャネルを利用しているGKEクラスタの場合、これらのバージョンのCHANGELOGを確認し、非互換性やアプリケーションへの影響がないかを評価してください。
*   GKEの自動アップグレードプロセスとメンテナンスウィンドウの設定を確認し、自動アップグレードに備えてください。
*   Google Cloud Composer 2をご利用の場合、Composerのメンテナンス期間中にGKEの自動アップグレードが行われる可能性が高いです。ワークロードへの影響を最小限に抑えるため、アップグレード前にアプリケーションの互換性テストを実施することを強く推奨します。

## Change
### The following versions are now available in the Regular channel:
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. The following versions are now available in the Regular channel: 1.31.14-gke.1114000, 1.32.9-gke.1675000, 1.33.5-gke.2019000.
説明：Regularリリースチャネルで、GKEバージョン1.31.14-gke.1114000、1.32.9-gke.1675000、1.33.5-gke.2019000が利用可能になりました。リリースノート公開時点でロールアウトが進行中であり、すべてのGoogle Cloudゾーンで利用可能になるまで数日かかる場合があります。
影響有無：**影響あり**。
Regularチャネルを利用しているGKEクラスタは、これらの新しいバージョンへの自動アップグレードの対象となります。Google Cloud Composer 2は通常RapidまたはRegularチャネルを利用するため、Composer環境の基盤GKEバージョンがこれらのバージョンに自動アップグレードされる可能性が高いです。
対処方法：
*   Regularチャネルを利用しているGKEクラスタの場合、これらのバージョンのCHANGELOGを確認し、非互換性やアプリケーションへの影響がないかを評価してください。
*   GKEの自動アップグレードプロセスとメンテナンスウィンドウの設定を確認し、自動アップグレードに備えてください。
*   Google Cloud Composer 2をご利用の場合、Composerのメンテナンス期間中にGKEの自動アップグレードが行われる可能性が高いです。ワークロードへの影響を最小限に抑えるため、アップグレード前にアプリケーションの互換性テストを実施することを強く推奨します。

## Change
### There are no new releases in the Stable channel.
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. There are no new releases in the Stable channel.
説明：Stableリリースチャネルでは、今回のリリースによる新しいバージョンの提供はありません。リリースノート公開時点でロールアウトが進行中であり、すべてのGoogle Cloudゾーンで利用可能になるまで数日かかる場合があります。
影響有無：**影響なし**。
Stableチャネルを利用しているGKEクラスタには、このリリースによる直接的なバージョン変更は発生しません。Google Cloud Composer 2がStableチャネルを利用している場合も、今回のリリースノートによる直接的な影響はありません。
対処方法：特になし。

---

### 用語説明

*   **GKE (Google Kubernetes Engine):** Google Cloudが提供するマネージドKubernetesサービスです。クラスタの管理、アップグレード、スケーリングなどの運用タスクをGoogleが代行するため、ユーザーはアプリケーションのデプロイと管理に集中できます。
*   **Container-Optimized OS (COS):** Google Cloudが提供する、コンテナ実行環境に最適化された仮想マシン（VM）イメージです。セキュリティとパフォーマンスに重点を置いて設計されており、GKEのノードイメージとして広く利用されます。
*   **リリースチャネル (Release Channel):** GKEクラスタのバージョンアップグレードの頻度と安定性を制御するための設定です。
    *   **Rapid (ラピッド):** 最新の機能が最も早く提供されますが、安定性は他のチャネルより劣る可能性があります。テスト環境や開発環境に適しています。
    *   **Regular (レギュラー):** バランスの取れた安定性と機能提供を提供します。多くの本番環境で利用されます。
    *   **Stable (ステーブル):** 最も安定性が高く、更新頻度が低いチャネルです。厳格な安定性が求められる本番環境に適しています。
    *   **Extended (エクステンデッド):** 特定のマイナーバージョンに対して長期的なサポートを提供するチャネルです。
*   **コントロールプレーン (Control Plane):** Kubernetesクラスタを管理する一連のコンポーネント（APIサーバー、スケジューラー、コントローラーマネージャーなど）の総称です。GKEでは、このコントロールプレーンはGoogleによって完全にマネージドされています。
*   **ノード (Node):** コンテナ化されたワークロード（Pod）が実際に実行される仮想マシンまたは物理マシンです。GKEでは、これらのノードはユーザーが選択したVMインスタンスタイプとOSイメージに基づいています。
*   **自動アップグレード (Auto-upgrade):** GKEクラスタのコントロールプレーンおよびノードが、選択したリリースチャネルとメンテナンスウィンドウの設定に従って自動的に新しいバージョンにアップグレードされる機能です。これにより、常に最新のセキュリティパッチと機能を利用できます。
*   **メンテナンスウィンドウ (Maintenance Window):** GKEの自動メンテナンス（アップグレードなど）が実行を許可される特定の時間帯を指定する設定です。これにより、ユーザーはサービスへの影響が最小限になるようにメンテナンス時間を制御できます。
*   **CHANGELOG:** ソフトウェアのリリースごとに加えられた変更点の記録。KubernetesのCHANGELOGは、各バージョンの詳細な変更内容（新機能、バグ修正、非互換性のある変更など）を確認するために重要です。