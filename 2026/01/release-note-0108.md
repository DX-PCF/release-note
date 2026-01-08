
# Title: January 05, 2026 
Link: https://docs.cloud.google.com/release-notes#January_05_2026<br>
# Google Cloud Composer 2 (基盤サービス: Google Kubernetes Engine)

## Change
### GKE cluster versions have been updated.
原文: GKE cluster versions have been updated. New versions available for upgrades and new clusters. The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.

説明: Google Kubernetes Engine (GKE) の新しいバージョンがリリースされ、新規クラスターの作成や既存クラスターのコントロールプレーンおよびノードのアップグレードに利用可能になりました。GKEのバージョニングおよびアップグレードに関する詳細情報は、公式ドキュメントで確認できます。

影響有無: なし。
理由: Google Cloud Composer 2はGoogleによってマネージドされているサービスであり、その基盤としてGKEクラスターを使用しています。GKEのバージョンアップはGoogle Cloud側でComposerのメンテナンスの一環として行われるため、お客様側で直接的な対応は不要です。これはGKEで利用可能なバージョンが増えたという情報であり、既存のComposer環境にすぐに影響を与えるものではありません。

対処方法: 特になし。

用語説明:
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するマネージドなKubernetesサービス。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **Composer (Google Cloud Composer)**: Apache AirflowをGoogle Cloud上でマネージドサービスとして提供するものです。ワークフローのオーケストレーションに使用されます。内部でGKEクラスターを使用してAirflowコンポーネントを実行します。
*   **コントロールプレーン (Control Plane)**: Kubernetesクラスターの制御層。APIサーバー、スケジューラー、コントローラーマネージャーなどが含まれ、クラスターの状態を管理します。
*   **ノード (Node)**: Kubernetesクラスターにおいて、アプリケーション（Pod）を実行するワーカーマシン。

## Security
### This release includes new GKE versions that use updated Container-Optimized OS images.
原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release. To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the Security release notes for that image.

説明: 本リリースに含まれる新しいGKEバージョンには、更新されたContainer-Optimized OS (COS) イメージが使用されています。これらのイメージは、前回のGKEリリース以降に公開された全てのCOSバージョンからのセキュリティ修正を累積的に含んでいます。特定の脆弱性に関する詳細については、各COSイメージのリリースノートを参照してください。

影響有無: 間接的にポジティブな影響。
理由: Composerの基盤であるGKEクラスターのノードOSがセキュリティ修正を含むCOSイメージに更新されることは、Composer環境全体のセキュリティ体制の向上に寄与します。これはGoogle Cloudによるマネージドサービスの標準的なセキュリティ更新プロセスの一部であり、お客様側での追加対応は不要です。

対処方法: 特になし。

用語説明:
*   **Container-Optimized OS (COS)**: Google Cloudが提供する、コンテナを実行するために最適化されたLinuxベースのオペレーティングシステム。GKEノードのデフォルトOSとして使用されます。セキュリティ、信頼性、パフォーマンスに重点が置かれています。

## Change
### New GKE versions available in various channels (Extended, Rapid, Regular, Stable)
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- The following versions are now available in the Extended channel: 1.28.15-gke.3285000, 1.29.15-gke.2617000, 1.30.14-gke.1861000
- The following versions are now available: 1.31.14-gke.1166000, 1.32.9-gke.1728000, 1.33.5-gke.2100000, 1.34.1-gke.3947000. The following node versions are now available: ... (same list as above)
- The following versions are now available in the Rapid channel: 1.31.14-gke.1166000, 1.32.9-gke.1728000, 1.33.5-gke.2100000, 1.34.1-gke.3947000, 1.35.0-gke.1340000
- The following versions are now available in the Regular channel: 1.31.14-gke.1114000, 1.32.9-gke.1675000, 1.33.5-gke.2019000
- There are no new releases in the Stable channel.

説明: GKEの各リリースチャネル（Extended, Rapid, Regular, Stable）で新しいバージョンが利用可能になりました。これらのバージョンは、ロールアウトが進行中であり、すべてのGoogle Cloudゾーンで利用可能になるまでに数日かかる場合があります。Stableチャネルには新たなリリースはありません。

影響有無: なし。
理由: Google Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3) の基盤GKEバージョンは、Google Cloudによって管理されており、通常はRegularまたはRapidチャネルのバージョンが使用されます。今回のリリースは、GKEで利用可能なバージョンが増えたという情報であり、既存のComposer環境に直接的な変更や互換性の問題をもたらすものではありません。Composerの基盤GKEは、Google Cloudのメンテナンスサイクルに従って順次更新されます。

対処方法: 特になし。

用語説明:
*   **リリースチャネル (Release Channel)**: GKEクラスターのリリースと更新の頻度を制御する設定。GKEにはStable、Regular、Rapid、Extendedなどのチャネルがあり、それぞれ更新の速さと安定性のバランスが異なります。
    *   **Stable チャネル**: 最も安定しており、機能の追加や変更が少ない。
    *   **Regular チャネル**: バランスの取れたチャネルで、定期的な更新と安定性を提供。Composerは通常このチャネルを使用。
    *   **Rapid チャネル**: 最新の機能が最も早く提供されるチャネル。新しい機能のテストや迅速な利用に適している。
    *   **Extended チャネル**: 特定の長期サポートバージョンを提供するチャネル。
*   **ロールアウト (Rollout)**: ソフトウェアや機能が段階的に展開されるプロセス。全ユーザーや全リージョンに一度に適用されるのではなく、時間をかけて順次展開されます。