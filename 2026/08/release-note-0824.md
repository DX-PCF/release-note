
# Title: August 21, 2026 
Link: https://docs.cloud.google.com/release-notes#August_21_2026<br>
Google Cloudのリリースノートに関する調査結果を以下に報告いたします。

---

# AlloyDB for PostgreSQL

## Fixed
原文: `AlloyDB now provides more accurate memory usage estimation, and it prevents out-of-memory (OOM) errors when you build a ScaNN four-level tree index. This feature is in Preview. This update improves the stability of index builds by enforcing memory limits and improving memory estimation under constrained conditions.`
説明：
AlloyDB for PostgreSQLにおいて、ScaNN four-level tree indexの構築時に発生するOut-of-Memory (OOM) エラーを防止するための改善が行われました。この機能は現在プレビュー段階ですが、メモリ使用量の推定精度が向上し、メモリ制限が適用されることで、インデックス構築の安定性が高まります。
影響有無：影響なし。
本変更は、ScaNN four-level tree indexの構築時の安定性を向上させるものであり、既存のワークロードに直接的な悪影響はありません。ScaNN indexを利用していない場合は、直接的な影響はありません。
対処方法：対応不要。
ScaNN indexを利用している場合、インデックス構築時の安定性が向上することを認識してください。

用語説明：
*   **AlloyDB for PostgreSQL**: Google Cloudが提供する、PostgreSQLと完全互換のフルマネージドなリレーショナルデータベースサービス。高性能、高可用性、AI/ML機能統合が特徴です。
*   **ScaNN (Scalable Nearest Neighbors)**: Googleが開発した大規模な近似近傍探索（ANN）のためのライブラリ。大量のベクトルデータから類似性の高いものを高速に検索する用途で使用されます。
*   **four-level tree index**: ScaNNが内部で使用するインデックス構造の一つで、効率的なデータ探索を実現するための階層構造です。
*   **Out-of-Memory (OOM) errors**: プログラムが利用可能なメモリを使い果たした際に発生するエラー。システムやアプリケーションの異常終了の原因となります。
*   **Preview**: Google Cloudの製品ライフサイクルにおける段階の一つ。一般提供（GA）前の状態であり、機能の検証やフィードバック収集を目的としています。本番環境での利用は推奨されない場合があります。

---

# Google Kubernetes Engine

## Change (リリースチャネルオプションの非推奨化)
原文: `Per the June 10, 2026 release note, the configuration option to not enroll your cluster in a release channel is deprecated, and will be removed on June 14, 2027. In alignment with this deprecation, creating new clusters not enrolled in a release channel is now only allowed for existing customers. New customers can use a release channel, where you can achieve the same functionality as not enrolling your cluster in a release channel. For more information, see Clusters not enrolled in a release channel.`
説明：
Google Kubernetes Engine (GKE) において、クラスターをリリースチャネルに登録しないオプションが非推奨化され、2027年6月14日に完全に削除されます。これに伴い、新規顧客はリリースチャネルに登録しないクラスターを作成できなくなります（既存顧客は引き続き作成可能です）。新規顧客はリリースチャネルを利用する必要があります。
影響有無：あり。
*   **既存顧客でリリースチャネルに登録していないGKEクラスターを利用している場合**: 2027年6月14日の機能削除期限までに、リリースチャネルへの移行を検討する必要があります。
*   **新規でGKEクラスターを構築する場合**: クラスターはリリースチャネルに登録する必要があります。過去にリリースチャネルに登録しない運用を行っていた場合、運用方針の見直しが必要です。
*   **既存顧客で既にリリースチャネルに登録しているGKEクラスターを利用している場合**: 直接的な影響はありません。
対処方法：
*   現在リリースチャネルに登録していないGKEクラスターを使用している場合、将来的な機能削除に備え、リリースチャネルへの移行計画を策定し、実行してください。移行には、現在のクラスターのバージョンアップポリシーの見直しや、場合によってはクラスターの再構築が必要になる可能性があります。
*   新規にGKEクラスターを構築する際は、リリースチャネルのいずれかを選択し、その運用ガイドラインに従うようにしてください。

用語説明：
*   **Google Kubernetes Engine (GKE)**: Google Cloudが提供するKubernetesのマネージドサービス。コンテナ化されたアプリケーションのデプロイ、スケーリング、管理を容易にします。
*   **リリースチャネル (Release Channel)**: GKEクラスタのバージョン更新ポリシーを管理する仕組みです。`Static`、`Regular`、`Stable`、`Rapid`などのチャネルがあり、それぞれ更新の頻度や安定性が異なります。これにより、ユーザーは自身のニーズに合った更新サイクルを選択できます。
*   **非推奨化 (Deprecated)**: 特定の機能やオプションが、将来的にサポートが終了する予定であることを示す状態です。既存の利用は可能ですが、新規利用は推奨されず、代替手段への移行が促されます。

---

# Google Kubernetes Engine

## Change (Windows Server 2019 (LTSC) ノードイメージの更新停止)
原文: `The Windows Server 2019 (LTSC) GKE node image doesn't receive updates after the December 2025 version. Windows Server 2019 (LTSC) is in the Extended Support period of the Microsoft fixed lifecycle policy and receives only security updates. To prevent stability issues, the GKE node image for Windows Server 2019 (LTSC) is pinned to the December 2025 version. If you use this node image, switch to Windows Server 2022 (LTSC), which is in the Mainstream Support period and receives updates from Microsoft and GKE. For more information, see Creating a cluster using Windows Server node pools.`
説明：
Google Kubernetes Engine (GKE) において、Windows Server 2019 (LTSC) のノードイメージは、2025年12月バージョン以降、GKEからの更新を受け取らなくなります。これは、Windows Server 2019 (LTSC) がMicrosoftの固定ライフサイクルポリシーにおける延長サポート期間に入り、セキュリティアップデートのみが提供されるためです。安定性の問題を避けるため、GKE上のWindows Server 2019 (LTSC) ノードイメージは2025年12月バージョンに固定されます。現在このノードイメージを使用している場合は、MicrosoftおよびGKEからのアップデートが継続されるWindows Server 2022 (LTSC) への移行が推奨されます。
影響有無：あり。
*   **Windows Server 2019 (LTSC) ノードイメージを使用しているGKEクラスター**: 2025年12月以降、OSレベルの機能アップデートやバグフィックスがGKEから提供されなくなり、将来的な安定性や新機能への対応に問題が生じる可能性があります。セキュリティアップデートはMicrosoftから継続されますが、GKEからの統合された更新は停止します。
*   **Windows Server 2022 (LTSC) またはLinuxノードを使用しているGKEクラスター**: 直接的な影響はありません。
対処方法：
*   現在Windows Server 2019 (LTSC) ノードイメージを使用しているGKEクラスターがある場合、2025年12月までにWindows Server 2022 (LTSC) ノードイメージへの移行計画を立て、実行してください。
*   移行は、既存のノードプールを新しいOSバージョンに更新するか、Windows Server 2022 (LTSC) を使用する新しいノードプールを作成し、ワークロードをそちらに移行する方法が考えられます。

用語説明：
*   **Windows Server (LTSC)**: Microsoftの長期サービスチャネル (Long-Term Servicing Channel) で提供されるWindows Serverのバージョン。長期にわたって安定した機能セットが提供され、主にセキュリティアップデートが継続的に提供されます。
*   **GKE node image**: GKEクラスタのワーカーノードとして使用される仮想マシン（VM）イメージ。OS、Kubernetesランタイム、GKEエージェントなどが含まれています。
*   **Microsoft fixed lifecycle policy**: Microsoft製品のサポート期間を定義するポリシー。`Mainstream Support`（メインストリームサポート）期間と`Extended Support`（延長サポート）期間があり、それぞれ提供されるサポート内容が異なります。
*   **Mainstream Support**: 製品の標準サポート期間。セキュリティアップデート、非セキュリティアップデート、有償サポートなどが提供されます。
*   **Extended Support**: メインストリームサポート終了後の延長サポート期間。主にセキュリティアップデートのみが提供されます。
# Title: August 20, 2026 
Link: https://docs.cloud.google.com/release-notes#August_20_2026<br>
## BigQuery
### Deprecated
原文: Starting April 26, 2027, core graph processing for BigQuery Graph will be restricted to the BigQuery Enterprise and Enterprise Plus editions. Consequently, we are deprecating support for Standard edition and on-demand billing for core graph processing. Graph measures will remain available in the Enterprise and Enterprise Plus editions and for queries run using on-demand pricing. Measures are not available in Standard edition.
説明: 2027年4月26日以降、BigQuery Graphのコアグラフ処理機能がBigQuery EnterpriseエディションおよびEnterprise Plusエディションに限定されることが発表されました。これにより、Standardエディションおよびオンデマンド課金でのコアグラフ処理のサポートは非推奨となります。ただし、Graph measures（グラフの統計量など）は、Enterprise/Enterprise Plusエディションおよびオンデマンド課金を引き続き利用できます。StandardエディションではGraph measuresは利用できません。
影響有無: **影響あり。**
現在BigQuery Standardエディションまたはオンデマンド課金でBigQuery Graphの**コアグラフ処理**を利用している場合、2027年4月26日以降、その機能が利用できなくなります。当社のシステムがBigQuery Graphのコアグラフ処理を頻繁に利用しており、Standardエディションまたはオンデマンド課金で運用されている場合、EnterpriseまたはEnterprise Plusエディションへの移行を検討する必要があります。
対処方法:
1.  **利用状況の確認**: BigQuery Graphのコアグラフ処理機能の利用状況を確認します。特にStandardエディションまたはオンデマンド課金モデルで利用しているかどうかを特定します。
2.  **影響範囲の評価**: BigQuery Graphの利用がビジネス上不可欠な処理であるか、または代替手段が可能かを評価します。
3.  **移行計画の策定**: コアグラフ処理の継続利用が必要な場合、BigQuery EnterpriseまたはEnterprise Plusエディションへの移行計画を策定し、2027年4月26日までに実行します。Graph measuresのみの利用であれば、Standardエディション以外のオンデマンド課金モデルでも引き続き利用可能です。
用語説明:
*   **BigQuery Graph**: BigQuery上でグラフデータ分析を行うための機能セット。ノードとエッジの関係性を分析し、パス検出、コミュニティ検出、中心性分析など高度なグラフアルゴリズムを実行できます。
*   **コアグラフ処理 (Core Graph Processing)**: BigQuery Graphの主要な機能で、複雑なグラフアルゴリズムを実行する部分。
*   **Graph measures (グラフメトリクス/統計量)**: グラフデータの基本的な統計情報や特性（ノード数、エッジ数、特定のノードの中心性など）を算出する機能。コアグラフ処理に比べて限定的な分析に利用されます。
*   **BigQuery Editions (エディション)**: BigQueryの料金体系と機能レベルを定義するモデル。Standard、Enterprise、Enterprise Plusなどのエディションがあり、それぞれ提供される機能、パフォーマンス、セキュリティ、料金が異なります。EnterpriseおよびEnterprise Plusは、より高度な機能やSLAを提供します。
*   **オンデマンド課金 (On-demand billing)**: BigQueryの料金モデルの一つで、クエリの実行ごとにスキャンされたデータ量に応じて課金される方式。

## Google Kubernetes Engine
### Change (GKEバージョンアップデート全体概要 & No channel (deprecated) )
原文: GKE cluster versions have been updated. New versions available for upgrades and new clusters. The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.
Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.35.6-gke.1710000 is now the default version for cluster creation.
- The following versions are now available: [list of available versions]
- The following node versions are now available: [list of available node versions]
- The following versions are no longer available: [list of no longer available versions including deprecated ones]
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: [list of auto-upgrade targets]
説明: GKEクラスタのバージョンが更新されました。新しいクラスタ作成や、既存クラスタのコントロールプレーンおよびノードのアップグレードに利用できる新しいバージョンが提供開始されました。一部のバージョンは非推奨となり、近い将来利用できなくなります。また、クラスタの自動アップグレードターゲットが更新されました。ロールアウトは進行中であり、全ゾーンに適用されるまでには数日かかる場合があります。
影響有無: **間接的な影響あり。**
Google Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3) はGKEクラスタ上で動作します。Composer 2.xは通常、GKEの特定のマイナーバージョン (例: 1.24/1.25) を利用しており、今回のリリースノートに記載されているGKEバージョン (1.31以降) は、現在のComposer環境が直接使用しているバージョンよりも新しい可能性が高いです。
ただし、GKEクラスタはセキュリティや安定性のため定期的に自動アップグレードされるため、将来的にこれらの新しいバージョンに追従する可能性があります。もし現在利用中のGKEクラスタバージョンが、今回「deprecated」（非推奨）または「no longer available」（利用不可）とされているバージョンに該当する場合、影響があります。現状、我々のComposer環境のGKEバージョンは、これらの非推奨バージョンには該当しないため、直接的な緊急対応は不要です。
対処方法:
1.  **GKEクラスタのバージョン確認**: 現在のComposer環境が利用しているGKEクラスタのバージョンを確認します。
2.  **非推奨バージョンへの合致確認**: 確認したバージョンが今回のリリースノートで「deprecated」または「no longer available」とされているリストに含まれていないことを確認します。含まれている場合は、将来的なアップグレード計画を検討します。
3.  **自動アップグレード設定の確認**: GKEクラスタの自動アップグレード設定（リリースチャネル、メンテナンスウィンドウ、除外設定）を確認し、将来のバージョンアップに備えて計画的な運用を継続します。
用語説明:
*   **コントロールプレーン (Control Plane)**: Kubernetesクラスタの管理ノード群。APIサーバー、スケジューラ、コントローラマネージャーなどから構成され、クラスタ全体の状態を管理します。
*   **ノード (Node)**: Kubernetesクラスタのワーカーマシン。アプリケーション（Pod）がデプロイされ、実行される物理または仮想マシンです。
*   **リリースチャネル (Release Channel)**: GKEクラスタのバージョン管理戦略。Rapid、Regular、Stable、Extendedの4つのチャネルがあり、それぞれ新しいバージョンの提供速度と安定性のバランスが異なります。我々のComposer環境のGKEは通常、これらのいずれかのチャネルに属しています。
*   **自動アップグレードターゲット (Auto-upgrade Targets)**: GKEが自動アップグレードを実行する際の、目標となるバージョン。

### Security (Container-Optimized OSイメージのセキュリティアップデート)
原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release. To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the Security release notes for that image.
説明: このリリースには、更新されたContainer-Optimized OS (COS) イメージを使用する新しいGKEバージョンが含まれています。これらのCOSイメージには、前回のGKEリリース以降に公開されたすべてのセキュリティ修正が累積的に適用されています。詳細な脆弱性情報は、各COSイメージのセキュリティリリースノートで確認できます。
影響有無: **影響なし（ポジティブな影響）。**
GKEノードが使用するContainer-Optimized OS (COS) イメージのセキュリティアップデートが含まれるため、これはクラスタのセキュリティ体制の向上につながります。既存のComposer環境はGKE上で稼働しており、GKEのノードは通常自動的に最新のCOSイメージに更新されるため、明示的な対処は不要ですが、セキュリティの強化という点で好ましい変更です。
対処方法:
1.  **確認**: GKEクラスタのノードが自動アップグレードされる設定になっていることを確認し、セキュリティパッチが適用される運用になっていることを確認します。
用語説明:
*   **Container-Optimized OS (COS)**: Googleによって最適化された、コンテナ実行に特化したLinuxベースのオペレーティングシステム。GKEノードのデフォルトOSとして利用されます。

### Change (Stable channel)
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- The following versions are now available in the Stable channel: [list of available versions]
- The following versions are no longer available in the Stable channel: [list of no longer available versions including deprecated ones]
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: [list of auto-upgrade targets]
説明: Stableリリースチャネルにおいて、利用可能なGKEバージョンが更新されました。新しいバージョンが提供され、いくつかの古いバージョンは非推奨または利用不可となりました。Stableチャネルのクラスタに対する自動アップグレードターゲットも更新されています。
影響有無: **影響なし。**
我々のComposer環境がどのGKEリリースチャネルに属しているかによって影響は異なりますが、もしStableチャネルを利用している場合、提供されるGKEバージョンが更新されます。現行のComposer 2.7.1が直接使用しているGKEバージョンが、今回Stableチャネルで非推奨となったバージョンリストに含まれていない限り、直接的な影響はありません。将来的なアップグレードパスに影響する可能性はあります。
対処方法:
1.  **確認**: Composer環境のGKEクラスタがStableチャネルを使用しているか確認します。
2.  **今後のアップグレード計画**: Stableチャネルを使用している場合、新しいバージョンの自動アップグレードターゲットを確認し、将来のアップグレードに備えます。

### Change (Regular channel)
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.35.6-gke.1710000 is now the default version for cluster creation in the Regular channel.
- The following versions are now available in the Regular channel: [list of available versions]
- The following versions are no longer available in the Regular channel: [list of no longer available versions including deprecated ones]
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: [list of auto-upgrade targets]
説明: Regularリリースチャネルにおいて、GKEバージョンが更新されました。新しいクラスタ作成のデフォルトバージョンが1.35.6-gke.1710000になり、新しいバージョンが提供され、いくつかの古いバージョンは非推奨または利用不可となりました。Regularチャネルのクラスタに対する自動アップグレードターゲットも更新されています。
影響有無: **影響なし。**
もし我々のComposer環境がRegularチャネルを利用している場合、提供されるGKEバージョンが更新されます。現行のComposer 2.7.1が直接使用しているGKEバージョンが、今回Regularチャネルで非推奨となったバージョンリストに含まれていない限り、直接的な影響はありません。将来的なアップグレードパスに影響する可能性はあります。
対処方法:
1.  **確認**: Composer環境のGKEクラスタがRegularチャネルを使用しているか確認します。
2.  **今後のアップグレード計画**: Regularチャネルを使用している場合、新しいバージョンの自動アップグレードターゲットを確認し、将来のアップグレードに備えます。

### Change (Rapid channel)
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.36.3-gke.1537000 is now the default version for cluster creation in the Rapid channel.
- The following versions are now available in the Rapid channel: [list of available versions]
- The following versions are no longer available in the Rapid channel: [list of no longer available versions including deprecated ones]
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: [list of auto-upgrade targets]
説明: Rapidリリースチャネルにおいて、GKEバージョンが更新されました。新しいクラスタ作成のデフォルトバージョンが1.36.3-gke.1537000になり、新しいバージョンが提供され、いくつかの古いバージョンは非推奨または利用不可となりました。Rapidチャネルのクラスタに対する自動アップグレードターゲットも更新されています。
影響有無: **影響なし。**
もし我々のComposer環境がRapidチャネルを利用している場合、提供されるGKEバージョンが更新されます。現行のComposer 2.7.1が直接使用しているGKEバージョンが、今回Rapidチャネルで非推奨となったバージョンリストに含まれていない限り、直接的な影響はありません。将来的なアップグレードパスに影響する可能性はあります。
対処方法:
1.  **確認**: Composer環境のGKEクラスタがRapidチャネルを使用しているか確認します。
2.  **今後のアップグレード計画**: Rapidチャネルを使用している場合、新しいバージョンの自動アップグレードターゲットを確認し、将来のアップグレードに備えます。

### Change (Extended channel)
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.35.6-gke.1710000 is now the default version for cluster creation in the Extended channel.
- The following versions are now available in the Extended channel: [list of available versions]
- The following versions are no longer available in the Extended channel: [list of no longer available versions including deprecated ones]
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: [list of auto-upgrade targets]
説明: Extendedリリースチャネルにおいて、GKEバージョンが更新されました。新しいクラスタ作成のデフォルトバージョンが1.35.6-gke.1710000になり、新しいバージョンが提供され、いくつかの古いバージョンは非推奨または利用不可となりました。Extendedチャネルのクラスタに対する自動アップグレードターゲットも更新されています。
影響有無: **影響なし。**
もし我々のComposer環境がExtendedチャネルを利用している場合、提供されるGKEバージョンが更新されます。現行のComposer 2.7.1が直接使用しているGKEバージョンが、今回Extendedチャネルで非推奨となったバージョンリストに含まれていない限り、直接的な影響はありません。将来的なアップグレードパスに影響する可能性はあります。
対処方法:
1.  **確認**: Composer環境のGKEクラスタがExtendedチャネルを使用しているか確認します。
2.  **今後のアップグレード計画**: Extendedチャネルを使用している場合、新しいバージョンの自動アップグレードターゲットを確認し、将来のアップグレードに備えます。