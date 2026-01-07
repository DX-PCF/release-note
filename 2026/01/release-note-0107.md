
# Title: January 05, 2026 
Link: https://docs.cloud.google.com/release-notes#January_05_2026<br>
# Google Kubernetes Engine

## Change
原文: GKE cluster versions have been updated. New versions available for upgrades and new clusters. The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.
説明: Google Kubernetes Engine (GKE) において、新しいクラスタバージョンが利用可能になりました。これらのバージョンは、新規GKEクラスタの作成、および既存クラスタのコントロールプレーンとノードの手動アップグレードの両方で利用できます。GKEのバージョン管理とアップグレードに関する詳細情報へのリンクも提供されています。
影響有無: 影響なし。
これは新しいGKEバージョンが利用可能になったというアナウンスであり、既存のクラスタや構成に直接的な影響を与えるものではありません。現在運用中のGoogle Cloud Composer 2 (Composer 2.7.1, Airflow 2.7.3) は、その基盤としてGKEを利用していますが、ComposerのGKEバージョンはComposerのライフサイクルによって管理されるため、この変更が直接Composer環境に影響を及ぼすことはありません。
対処方法: 特に対処は不要です。将来的なGKEクラスタの新規構築や手動アップグレードを検討する際に、これらの新しいバージョンを選択肢として考慮できます。

## Security
原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release. To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the Security release notes for that image. The following table includes links to the release notes for each updated Container-Optimized OS image: GKE version 1.35.0-gke.1340000 Container-Optimized OS version cos-125-19216-104-45 Details cos-125-19216-104-45 release notes
説明: 今回のGKEリリースに含まれる新しいバージョンでは、Container-Optimized OS (COS) の最新のセキュリティ修正が適用されたイメージが利用されています。これにより、GKEクラスタのノードのセキュリティが向上します。具体的な脆弱性の修正内容については、各COSイメージのリリースノートを参照してください。
影響有無: 影響なし（ポジティブな影響）。
これはGKEノードの基盤となるOSのセキュリティ強化に関するアップデートであり、既存環境のセキュリティ体制が向上する可能性があります。Google Cloud Composer 2はGKEノード上で動作するため、間接的にその基盤のセキュリティが強化されることになります。
対処方法: 特に対処は不要です。GKEクラスタの自動アップグレードやノードの自動修復機能が有効な場合、これらのセキュリティパッチが適用されたOSイメージが自動的に適用されます。

## Change
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. - The following versions are now available in the Extended channel: - 1.28.15-gke.3285000 - 1.29.15-gke.2617000 - 1.30.14-gke.1861000
説明: GKEのExtendedリリースチャンネルで、以下の新しいバージョンが利用可能になりました。ただし、これらのバージョンがすべてのGoogle Cloudゾーンで完全に展開されるまでには数日かかる場合があります。
*   1.28.15-gke.3285000
*   1.29.15-gke.2617000
*   1.30.14-gke.1861000
影響有無: 影響なし。
これは特定のリリースチャンネルで利用可能なGKEバージョンのリストが更新されたものであり、既存のGKEクラスタの動作に直接的な影響はありません。Google Cloud Composer 2環境は、GKEのバージョンがComposerのアップグレードによって管理されるため、この情報が直接的な運用上の影響を与えることはありません。
対処方法: 特に対処は不要です。

## Change
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. - The following versions are now available: - 1.31.14-gke.1166000 - 1.32.9-gke.1728000 - 1.33.5-gke.2100000 - 1.34.1-gke.3947000 - The following node versions are now available: - 1.28.15-gke.3285000 - 1.29.15-gke.2617000 - 1.30.14-gke.1861000 - 1.31.14-gke.1166000 - 1.32.9-gke.1728000 - 1.33.5-gke.2100000 - 1.34.1-gke.3947000
説明: GKEクラスタとノードプールで、以下の新しいバージョンが利用可能になりました。これらのバージョンは、全てのGoogle Cloudゾーンで展開されるまでに数日かかる場合があります。
*   利用可能なクラスタバージョン:
    *   1.31.14-gke.1166000
    *   1.32.9-gke.1728000
    *   1.33.5-gke.2100000
    *   1.34.1-gke.3947000
*   利用可能なノードバージョン:
    *   1.28.15-gke.3285000
    *   1.29.15-gke.2617000
    *   1.30.14-gke.1861000
    *   1.31.14-gke.1166000
    *   1.32.9-gke.1728000
    *   1.33.5-gke.2100000
    *   1.34.1-gke.3947000
影響有無: 影響なし。
これは利用可能なGKEクラスタおよびノードプールのバージョンが追加されたことを示すもので、既存環境に直接的な変更をもたらすものではありません。Google Cloud Composer 2環境への直接的な影響はありません。
対処方法: 特に対処は不要です。

## Change
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. - The following versions are now available in the Rapid channel: - 1.31.14-gke.1166000 - 1.32.9-gke.1728000 - 1.33.5-gke.2100000 - 1.34.1-gke.3947000 - 1.35.0-gke.1340000
説明: GKEのRapidリリースチャンネルで、以下の新しいバージョンが利用可能になりました。これらのバージョンがすべてのGoogle Cloudゾーンで完全に展開されるまでには数日かかる場合があります。
*   1.31.14-gke.1166000
*   1.32.9-gke.1728000
*   1.33.5-gke.2100000
*   1.34.1-gke.3947000
*   1.35.0-gke.1340000
影響有無: 影響なし。
Rapidチャンネルにおける利用可能バージョンの更新であり、既存のGKEクラスタやGoogle Cloud Composer 2環境に直接的な影響はありません。
対処方法: 特に対処は不要です。

## Change
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. - The following versions are now available in the Regular channel: - 1.31.14-gke.1114000 - 1.32.9-gke.1675000 - 1.33.5-gke.2019000
説明: GKEのRegularリリースチャンネルで、以下の新しいバージョンが利用可能になりました。これらのバージョンがすべてのGoogle Cloudゾーンで完全に展開されるまでには数日かかる場合があります。
*   1.31.14-gke.1114000
*   1.32.9-gke.1675000
*   1.33.5-gke.2019000
影響有無: 影響なし。
Regularチャンネルにおける利用可能バージョンの更新であり、既存のGKEクラスタやGoogle Cloud Composer 2環境に直接的な影響はありません。
対処方法: 特に対処は不要です。

## Change
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. There are no new releases in the Stable channel.
説明: GKEのStableリリースチャンネルでは、今回のリリースにおいて新しいバージョンの追加はありません。
影響有無: 影響なし。
Stableチャンネルで変更がないことを示すアナウンスであり、既存のGKEクラスタやGoogle Cloud Composer 2環境に影響はありません。
対処方法: 特に対処は不要です。

---
**用語説明**

*   **Google Kubernetes Engine (GKE)**: Google Cloudが提供するマネージドKubernetesサービスであり、コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを自動化します。
*   **Container-Optimized OS (COS)**: Google CloudでGKEノードとして動作するために最適化されたLinuxベースのオペレーティングシステムです。セキュリティ、安定性、パフォーマンスに重点を置いています。
*   **GKE リリースチャンネル (Release Channel)**: GKEクラスタのバージョンと機能の展開ペースを制御するための設定です。`Rapid`、`Regular`、`Stable`、`Extended`の4つのチャンネルがあり、それぞれに異なるアップグレードポリシーと安定性の特性があります。
    *   **Rapid channel**: 最新のGKEバージョンが最も早く提供されますが、変更頻度も高いです。
    *   **Regular channel**: Rapidよりも安定性が高く、機能と安定性のバランスが取れており、ほとんどのワークロードに適しています。
    *   **Stable channel**: 最も安定性が高く、重要な修正のみが提供されます。
    *   **Extended channel**: 長期的なサポートを目的とし、特定のマイナーバージョンが長期間提供されます。
*   **コントロールプレーン (Control Plane)**: Kubernetesクラスタの「頭脳」にあたる部分で、APIサーバー、スケジューラー、コントローラーマネージャーなどが含まれます。クラスタの状態を管理し、ノード上のワークロードを制御します。
*   **ノード (Node)**: Kubernetesクラスタ内のワーカーマシンであり、Podがデプロイされる場所です。Container-Optimized OSなどのオペレーティングシステムが動作しています。
*   **Google Cloud Composer**: Google Cloudが提供するApache Airflowのマネージドサービスです。ワークフローのオーケストレーションに使用され、内部的にはGKEクラスタを基盤として利用しています。
*   **Kubernetes バージョニング**: Kubernetesのバージョンは一般的に「MAJOR.MINOR.PATCH」の形式で表されます。GKEバージョンはこれにGKE固有のサフィックス（例: `-gke.XXXXXXX`）が付与されます。