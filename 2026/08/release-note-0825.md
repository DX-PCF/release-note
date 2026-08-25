
# Title: August 21, 2026 
Link: https://docs.cloud.google.com/release-notes#August_21_2026<br>
Google Cloudのリリースノートに対する影響調査結果を以下に示します。

# AlloyDB for PostgreSQL
## Fixed
原文: AlloyDB now provides more accurate memory usage estimation, and it prevents out-of-memory (OOM) errors when you build a ScaNN four-level tree index. This feature is in Preview. This update improves the stability of index builds by enforcing memory limits and improving memory estimation under constrained conditions.

[four-level tree index](https://docs.cloud.google.com/alloydb/docs/ai/create-scann-index#create-scann-index-manual)
[Preview](https://cloud.google.com/products#product-launch-stages)
For more information, see Create a ScaNN index.

[Create a ScaNN index](https://docs.cloud.google.com/alloydb/docs/ai/create-scann-index#create-scann-index-manual)

説明: AlloyDB for PostgreSQLにおいて、ベクトル検索機能であるScaNNのfour-level tree index構築時のメモリ使用量の見積もり精度が向上しました。これにより、メモリ不足（OOM）エラーの発生が抑制され、メモリ制約下でのインデックス構築の安定性が改善されました。この機能は現在プレビュー版として提供されています。
影響有無: なし
理由: 本変更は、ScaNN four-level tree index構築時の既知の問題（OOMエラー）に対する修正であり、機能の安定性向上を目的としています。この機能は現在プレビュー段階であり、利用している場合はポジティブな影響（安定性向上）があります。利用していない場合は直接的な影響はありません。
対処方法: 特になし。もしScaNN four-level tree indexの構築でOOMエラーに悩まされていた場合、今回の修正により問題が解消される可能性があります。
用語説明:
*   **ScaNN (Scalable Nearest Neighbors)**: Googleが開発した、大規模なデータセットから類似するデータを高速に検索するためのライブラリ。主にベクトル検索（Vector Search）に利用され、AlloyDBではAI機能の一部として統合されています。
*   **four-level tree index**: ScaNNで利用されるインデックス構造の一つ。階層的なツリー構造を用いて、大規模なデータセットの中から効率的に類似する点を検索するために設計されています。
*   **OOM (Out-Of-Memory) エラー**: プログラムやシステムが利用可能なメモリを使い果たした際に発生するエラー。この場合、インデックス構築プロセスが異常終了する原因となります。
*   **Preview (プレビュー)**: Google Cloudにおける製品のローンチステージの一つ。一般提供（GA: General Availability）の前段階で、機能がまだ完全に安定しておらず、変更される可能性があることを示します。本番環境での利用は推奨されない場合が多いですが、テストや評価のために提供されます。

# Google Kubernetes Engine
## Change
原文: Per the June 10, 2026 release note, the configuration option to not enroll your cluster in a release channel is deprecated, and will be removed on June 14, 2027. In alignment with this deprecation, creating new clusters not enrolled in a release channel is now only allowed for existing customers. New customers can use a release channel, where you can achieve the same functionality as not enrolling your cluster in a release channel. For more information, see Clusters not enrolled in a release channel.

[June 10, 2026 release note](#June_10_2026)
[Clusters not enrolled in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel)

説明: GKEクラスターをリリースチャネルに登録しない（"No channel"）という設定オプションが非推奨（Deprecated）となり、2027年6月14日には完全に削除される予定です。この変更に伴い、新規顧客はリリースチャネルに登録しないクラスターを作成することができなくなりました。既存顧客は引き続き作成可能ですが、Googleはリリースチャネルを使用することで「No channel」と同様の機能を実現できると説明しています。
影響有無: 利用状況によって影響あり
理由: 現在「No channel」設定でGKEクラスターを運用している場合、将来的なサポート終了に向けて移行計画が必要です。また、今後GKEクラスターを新規作成する際に、「No channel」オプションを選択できなくなる可能性があるため、リリースチャネル利用を前提とした運用方針への見直しが必要となります。
対処方法:
1.  **既存の「No channel」GKEクラスターについて**: 2027年6月14日のサポート終了までに、リリースチャネルへの移行を計画してください。Googleの公式ドキュメント「Clusters not enrolled in a release channel」を参照し、適切なリリースチャネルへの移行パスや代替手段を検討してください。
2.  **新規GKEクラスターの作成について**: 今後クラスターを作成する際は、リリースチャネル（例: `Rapid`, `Regular`, `Stable`）を利用することを標準としてください。新規顧客はこの選択が必須となります。
用語説明:
*   **リリースチャネル (Release Channel)**: GKEクラスターのアップグレードポリシーを管理するための仕組みです。`Rapid`、`Regular`、`Stable`の3つのチャネルがあり、それぞれ異なる速度で新しいGKEバージョンが提供されます。ユーザーは安定性、新機能の利用、または最新機能へのアクセスのバランスを選択できます。
*   **非推奨 (Deprecated)**: 将来的にサポートが終了するか、削除される予定の機能や設定を示します。通常、代替機能が提供され、ユーザーは指定された期間内に移行することが推奨されます。
*   **No channel (リリースチャネルに登録しない)**: GKEクラスターを特定のリリースチャネルに登録しない設定。これにより、ユーザーはGKEバージョンのアップグレードを完全に手動で管理できますが、自動アップグレードやGoogleによる運用支援の恩恵を受けにくくなります。

## Change
原文: The Windows Server 2019 (LTSC) GKE node image doesn't receive updates after the December 2025 version. Windows Server 2019 (LTSC) is in the Extended Support period of the Microsoft fixed lifecycle policy and receives only security updates. To prevent stability issues, the GKE node image for Windows Server 2019 (LTSC) is pinned to the December 2025 version. If you use this node image, switch to Windows Server 2022 (LTSC), which is in the Mainstream Support period and receives updates from Microsoft and GKE. For more information, see Creating a cluster using Windows Server node pools.

[fixed lifecycle policy](https://learn.microsoft.com/en-us/lifecycle/policies/fixed)
[Creating a cluster using Windows Server node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows)

説明: GKEのWindows Server 2019 (LTSC) ノードイメージは、2025年12月以降、GKEからの更新（機能アップデートなど）を受け取らなくなります。これは、Windows Server 2019 (LTSC) がMicrosoftのライフサイクルポリシーにおける拡張サポート期間に入り、セキュリティアップデートのみが提供されるためです。安定性の問題を避けるため、GKEにおけるWindows Server 2019 (LTSC) のノードイメージは2025年12月バージョンで固定されます。このノードイメージを使用している場合、MicrosoftおよびGKEからのアップデートを継続して受け取れるWindows Server 2022 (LTSC) への移行が推奨されます。
影響有無: Windows Server 2019 (LTSC) を利用したGKEノードプールを使用している場合、影響あり
理由: 2025年12月以降、Windows Server 2019 (LTSC) ノードイメージはGKEからの機能改善やパフォーマンス向上に関するアップデートを受けられなくなります。これにより、最新のGKE機能や最適化の恩恵を受けられず、将来的な安定性や互換性の問題が発生する可能性があります。
対処方法:
1.  現在、GKEでWindows Server 2019 (LTSC) を使用しているノードプールが存在する場合、Windows Server 2022 (LTSC) を使用する新しいノードプールへの移行を計画してください。
2.  移行前に、既存のWindowsワークロードがWindows Server 2022 (LTSC) 環境で正常に動作するか、互換性テストを実施することをお勧めします。
3.  詳細な移行手順については、GKEのドキュメント「Creating a cluster using Windows Server node pools」を参照してください。
用語説明:
*   **LTSC (Long-Term Servicing Channel)**: Microsoft Windows Serverのリリースモデルの一つで、長期的な安定性と互換性を重視し、機能アップデートの頻度が少ないのが特徴です。主に基幹システムや特定用途のサーバー向けに設計されています。
*   **ノードイメージ (Node Image)**: GKEクラスターの各ワーカーノードで実行されるオペレーティングシステム（OS）のイメージファイルです。これには、OS、Kubernetesコンポーネント、コンテナランタイムなどが含まれます。
*   **Microsoft 固定ライフサイクルポリシー (Microsoft Fixed Lifecycle Policy)**: Microsoft製品のサポート期間を定義するポリシーです。通常、新機能や無償サポートが含まれる「メインストリームサポート」期間と、主に無償のセキュリティアップデートのみが提供される「拡張サポート」期間があります。
*   **メインストリームサポート (Mainstream Support)**: Microsoftのライフサイクルポリシーにおける初期段階のサポート。新機能、セキュリティ更新プログラム、セキュリティ以外の更新プログラム、無償サポートなどが提供されます。
*   **拡張サポート (Extended Support)**: メインストリームサポート期間終了後に続くサポート期間。主に無償のセキュリティ更新プログラムのみが提供され、新機能や非セキュリティの修正は含まれません。