
# Title: June 12, 2026 
Link: https://docs.cloud.google.com/release-notes#June_12_2026<br>
はい、承知いたしました。Google Cloudのリリースノートを基に、構築済みのGoogle Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) への影響有無を調査し、簡潔に回答します。

---

# Cloud Monitoring
## Change
原文: All `agent.googleapis.com/processes` metrics are retained for 24 months. For more information, see Data retention.

説明:
Google Cloud Monitoring において、`agent.googleapis.com/processes` に関連するすべてのメトリクスのデータ保持期間が、これまでの6週間から24ヶ月に延長されました。これにより、より長期間のプロセス関連のメトリクスデータを分析できるようになります。

影響有無:
**影響なし（ポジティブな影響）**
`agent.googleapis.com/processes` メトリクスの保持期間が延長されるだけであり、既存の監視設定やデータ収集には影響ありません。むしろ、過去のパフォーマンスデータをより長期間にわたって確認できるようになるため、長期的なトレンド分析やトラブルシューティングにおいて有益です。Google Cloud Composer の監視には影響を与えません。

対処方法:
特になし。自動的に適用されます。

用語説明:
*   **Google Cloud Monitoring**: Google Cloud上のアプリケーションやインフラストラクチャのパフォーマンス、可用性、状態を監視するためのサービス。
*   **メトリクス**: システムやアプリケーションのパフォーマンスや状態を示す数値データ。例としてCPU使用率、メモリ使用量、プロセス数など。
*   **データ保持期間**: 監視データが保存される期間。この期間を過ぎるとデータは削除されるか、低解像度で保持されます。

---

# Cloud Service Mesh
## Security
原文: The following images are now rolling out for managed Cloud Service Mesh:
- Sidecar version 1.21.6-asm.36, is rolling out to the rapid release channel.
- Sidecar version 1.20.8-asm.86 is rolling out to the regular release channel.
- Sidecar version 1.19.10-asm.76 is rolling out to the stable release channel.
These rollouts will preempt those previously announced on June 3, 2026.
These patch releases contain the fix for the vulnerability listed in GCP-2026-035

説明:
マネージドCloud Service Mesh向けに、サイドカープロキシの新しいパッチバージョン（1.21.6-asm.36、1.20.8-asm.86、1.19.10-asm.76）が、各リリースチャネル（rapid、regular、stable）に展開されています。これらのリリースには、脆弱性GCP-2026-035に対する修正が含まれています。

## Security
原文: Proxy version csm_mesh_proxy.20260423_RC03 for Gateway API on GKE clusters is rolling out to all Managed Cloud Service Mesh release channels over the next week.

説明:
GKEクラスタ上のGateway APIで使用されるプロキシ（csm_mesh_proxy.20260423_RC03）が、今後1週間かけてすべてのマネージドCloud Service Meshリリースチャネルに展開されます。

影響有無:
**影響なし**
Google Cloud Composer 2は通常、Cloud Service Meshを直接利用しません。したがって、Cloud Service Meshのサイドカーやプロキシのバージョンアップは、Composer環境には直接的な影響を与えません。マネージドサービスであるため、Service Meshユーザーにとっても自動的にロールアウトされる変更であり、手動での対処は不要です。

対処方法:
特になし。

用語説明:
*   **Cloud Service Mesh**: Google Cloudが提供するIstioベースのマネージドサービスメッシュソリューション。マイクロサービス間の通信管理、トラフィックルーティング、セキュリティポリシー適用などを行います。
*   **サイドカー (Sidecar)**: サービスメッシュの文脈では、アプリケーションコンテナと連携して動作し、ネットワーク通信の制御や監視を行うためのプロキシコンテナ。IstioではEnvoyプロキシが使用されます。
*   **リリースチャネル**: Google Cloudのサービス（特にGKEやService Meshなど）において、新しいバージョンの機能や修正がどの程度の速度で提供されるかを定義する区分。Rapid（最速）、Regular（標準）、Stable（安定版）、Extended（長期サポート版）などがあります。
*   **GCP-2026-035**: 特定の脆弱性識別子。この番号で関連するセキュリティ情報が公開されます。
*   **Gateway API**: Kubernetesにおいて、クラスタのイングレスおよびエグレスのトラフィックルーティングを管理するための新しいAPI（従来のIngress APIの後継）。

---

# Google Kubernetes Engine
## Change
原文: GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.

## No channel (deprecated)
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.35.5-gke.1000000 is now the default version for cluster creation.
- The following versions are now available: (...)
- The following node versions are now available: (...)
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: (...)

## Security
原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release.
To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the Security release notes for that image. The following table includes links to the release notes for each updated Container-Optimized OS image: (...)

## Change (Stable channel)
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- The following versions are now available in the Stable channel: (...)
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: (...)

## Change (Regular channel)
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.35.5-gke.1000000 is now the default version for cluster creation in the Regular channel.
- The following versions are now available in the Regular channel: (...)
- The following versions are no longer available in the Regular channel: (...)
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: (...)

## Change (Rapid channel)
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.36.0-gke.2684000 is now the default version for cluster creation in the Rapid channel.
- The following versions are now available in the Rapid channel: (...)
- The following versions are no longer available in the Rapid channel: (...)
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: (...)

## Change (Extended channel)
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.35.5-gke.1000000 is now the default version for cluster creation in the Extended channel.
- The following versions are now available in the Extended channel: (...)
- The following versions are no longer available in the Extended channel: (...)
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: (...)

説明:
Google Kubernetes Engine (GKE) の複数のリリースチャネル（No channel (deprecated), Stable, Regular, Rapid, Extended）において、利用可能なGKEクラスターバージョンが更新されました。これには、新しいデフォルトバージョンの設定、アップグレードターゲットの変更、およびノードバージョンが含まれます。また、これらの新しいGKEバージョンは、セキュリティ修正が適用された最新のContainer-Optimized OS (COS) イメージを使用しています。一部の古いバージョンは非推奨となり、90日後に削除される予定です。

影響有無:
**間接的な影響あり（ポジティブな影響が主）**
Google Cloud Composer 2 は、内部的にGKEクラスター上で動作しています。したがって、GKEのバージョン更新はComposer 2の基盤に影響を与えます。

1.  **セキュリティと安定性の向上**: 新しいGKEバージョンには、Container-Optimized OSのセキュリティ修正が含まれており、基盤のセキュリティと安定性が向上します。これはComposer環境にとってもポジティブな影響です。
2.  **自動アップグレード**: Composerはマネージドサービスであるため、GKEクラスターのバージョンアップグレードはGoogleによって管理されます。ユーザーが直接GKEクラスターを手動でアップグレードする必要はありません。Composerのメンテナンスウィンドウ設定やリリースチャネルに基づいて、適切なタイミングで基盤のGKEバージョンが更新される可能性があります。
3.  **互換性**: 通常、ComposerがサポートするAirflowバージョン（今回の場合2.7.3）は、Googleが提供するGKEバージョンと互換性が保たれるように管理されています。GKEのマイナーバージョンアップにより、Kubernetes APIの変更などが発生する可能性はありますが、Composer環境内で動作するAirflowアプリケーションやDAG (Directed Acyclic Graph) が直接的な非互換性の影響を受ける可能性は低いと考えられます。ただし、カスタムのPythonパッケージやオペレータで非常に古いKubernetes APIを利用している場合など、まれに影響が出る可能性はゼロではありません。
4.  **非推奨バージョン**: GKEの非推奨バージョンが記載されています。もしComposer環境の基盤となるGKEバージョンがこれらの非推奨バージョンに該当する場合、将来的にGoogleによる強制的なアップグレードの対象となる可能性があります。しかし、これもComposerのマネージドサービスとして適切に処理されるため、ユーザー側での緊急の対処は不要です。

対処方法:
1.  **ComposerのGKEバージョン確認**: 現在ご利用のComposer環境がどのGKEバージョン上で動作しているかを確認します。通常、Composerの環境情報から確認可能です。
2.  **Composerのリリースノート確認**: Composer自身のリリースノートやドキュメントを定期的に確認し、ComposerがサポートするGKEバージョンや、Composerのバージョンアップグレードに伴う基盤GKEの変更に関する情報に注意を払うことを推奨します。
3.  **非互換性の懸念**: GKEのメジャーバージョンアップ（例: 1.x から 1.y）に伴い、AirflowのカスタムDAGsや利用しているツール、ライブラリとの潜在的な非互換性がないか、Composerのメンテナンスウィンドウを考慮しつつ、必要に応じてテスト環境で検証を検討することが望ましいです。ただし、GKEのバージョンアップはGoogle Cloud Composerによって管理されているため、通常はComposerのアップグレードプロセスの一部として互換性が検証されます。

用語説明:
*   **Google Kubernetes Engine (GKE)**: Google Cloudが提供するフルマネージドのKubernetesサービス。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **Google Cloud Composer**: Apache AirflowをGoogle Cloud上で実行するためのフルマネージドサービス。ワークフローのオーケストレーションに使用されます。GKEを基盤としています。
*   **コントロールプレーン**: Kubernetesクラスターの「脳」にあたる部分で、APIサーバー、スケジューラ、コントローラマネージャー、etcdなどで構成され、クラスター全体の状態を管理します。
*   **ノード**: Kubernetesクラスター内でアプリケーションワークロード（コンテナ）を実行するワーカーマシン。
*   **Container-Optimized OS (COS)**: Google Cloudが提供する、Kubernetesコンテナワークロードの実行に最適化された最小限のオペレーティングシステム。セキュリティと安定性に優れています。
*   **リリースチャネル**: GKEクラスターのバージョンアップグレードのポリシーを決定する設定。Rapid、Regular、Stable、Extendedなどがあり、それぞれ新機能の導入速度と安定性のバランスが異なります。
*   **自動アップグレードターゲット**: GKEクラスターが自動アップグレードによって到達する目標バージョン。
*   **メンテナンス除外期間 (maintenance exclusions)**: GKEの自動アップグレードやその他のメンテナンス作業を指定した期間中に実行しないように設定する機能。
*   **非推奨 (deprecated)**: 将来のバージョンでサポートが終了する、または削除される予定であることを示す状態。