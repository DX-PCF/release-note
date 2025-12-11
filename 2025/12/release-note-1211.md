
# Title: December 10, 2025 
Link: https://docs.cloud.google.com/release-notes#December_10_2025<br>
# Apigee X

## Announcement

原文: On December 10th, 2025, we released an updated version of Apigee (1-16-0-apigee-6).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明：
2025年12月10日にApigeeの新しいバージョン (1-16-0-apigee-6) がリリースされました。
このリリースの展開は本日から開始されており、Google Cloudの全ゾーンで完了するまでに4営業日以上かかる場合があります。そのため、お客様のApigeeインスタンスによっては、展開が完了するまでは新機能や修正が利用できない可能性があります。

影響有無：
**影響あり**。
ApigeeはSaaSサービスであるため、新しいバージョンへの自動更新が行われます。これは一般的なクラウドサービスのアップデートプロセスであり、基本的にはユーザー側でのアクションは不要ですが、新機能や修正が全てのインスタンスに反映されるまでに時間差が生じることに留意が必要です。特定の機能修正や改善に依存するAPIプロキシのデプロイを計画している場合、展開完了を待つ必要があります。

対処方法：
特にユーザー側での対処は不要です。Apigeeインスタンスは自動的に新しいバージョンに更新されます。ただし、特定の修正や機能に依存する運用を行っている場合は、リリース展開が完了し、それらの変更が利用可能になったことを確認してから、関連する変更を適用することを推奨します。

用語説明：
*   **Apigee**: APIの設計、開発、公開、セキュリティ、監視、分析を可能にするGoogle CloudのAPI管理プラットフォームです。Apigee Xは、Google Cloudのインフラストラクチャ上で動作するSaaS（Software as a Service）版Apigeeを指します。
*   **Rollout (リリース展開)**: 新しいソフトウェアバージョンや機能が、システム全体または特定のユーザーグループに段階的に導入されるプロセスを指します。安定性や影響を考慮して、即座に全ての環境に適用されるのではなく、時間をかけて行われます。

## Fixed

原文:
| Bug ID | Description |
| --- | --- |
| **458417250** | **Multiple authorization headers** Fixed issue where adding multiple authorization headers would cause Apigee to return a `500` error. |
| **N/A** | **Updates to security, infrastructure, and libraries.** |

説明：
以下の問題が修正されました。
*   複数の認可ヘッダー (Authorization headers) をAPIリクエストに追加すると、ApigeeがHTTP 500エラーを返す不具合が修正されました。(Bug ID: 458417250)
*   セキュリティ、インフラストラクチャ、および基盤となるライブラリが更新されました。

影響有無：
**影響あり（改善）**。
*   もし、お客様のAPIプロキシや統合が複数の認可ヘッダーを使用するシナリオでApigeeが500エラーを返していた場合、この修正により問題が解決し、APIの信頼性および可用性が向上します。
*   セキュリティ、インフラストラクチャ、およびライブラリの更新は、Apigeeプラットフォーム全体の安定性、パフォーマンス、およびセキュリティ体制の向上に寄与します。

対処方法：
特にユーザー側での対処は不要です。Apigeeインスタンスが新しいバージョンに自動更新されることで、これらの修正が適用されます。
複数の認可ヘッダーを使用するAPIプロキシを運用しており、これまで500エラーに遭遇していた場合は、今回のアップデート後に動作が改善されていることを確認してください。

用語説明：
*   **Authorization headers (認可ヘッダー)**: HTTPリクエストヘッダーの一つで、クライアントがサーバーに対して認証情報（例: APIキー、OAuthトークン、JWTなど）を提示するために使用されます。これにより、サーバーはリクエストの送信元を特定し、アクセス制御ポリシーを適用します。
*   **HTTP 500 Internal Server Error**: サーバーがリクエストを処理しようとして、予期しない内部エラーが発生したことを示すHTTPステータスコードです。これはサーバー側の問題を示し、クライアントのリクエスト自体に問題があるわけではありません。
*   **Libraries (ライブラリ)**: ソフトウェア開発において、特定の機能やタスクを効率的に実現するために再利用可能なコードの集合体です。通常、API、クラス、関数などの形で提供されます。今回の更新は、Apigeeの基盤となるソフトウェアコンポーネントの改善を指します。
# Title: December 08, 2025 
Link: https://docs.cloud.google.com/release-notes#December_08_2025<br>
はい、承知いたしました。Google Kubernetes Engine のリリースノートについて、製品への影響調査を行います。

---

# Google Kubernetes Engine

## Fixed

原文:
The October 14, 2025 issue in which MountVolume calls for network file system (NFS) volumes might fail is fixed for GKE versions 1.34.1-gke.2877000 and later.
[October 14, 2025](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#October_14_2025)

説明：
本リリースノートは、2025年10月14日に発生する可能性があった、NFS (Network File System) ボリュームへの `MountVolume` 呼び出しが失敗する問題が修正されたことをアナウンスしています。この修正は、GKEバージョン `1.34.1-gke.2877000` およびそれ以降のバージョンに適用されています。これは、将来的に発生が見込まれていた潜在的なバグが、対象バージョンで事前に解決されたことを意味します。

影響有無：
利用しているGKEクラスターがNFSボリュームを使用しているかどうか、および現在のクラスターバージョンによって影響が異なります。

*   **影響あり（または将来的な影響を回避可能）：**
    *   現在、NFSボリュームをGKEクラスターで使用しており、かつクラスターのバージョンが `1.34.1-gke.2877000` より**古い**場合、将来的にこの問題の影響を受ける可能性があります。この修正が適用されるバージョンにアップグレードすることで、問題の発生を未然に防ぐことができます。
*   **影響なし：**
    *   NFSボリュームをGKEクラスターで**使用していない**場合、この修正は直接的な影響を与えません。
    *   現在NFSボリュームを使用しており、かつクラスターのバージョンが既に `1.34.1-gke.2877000` **以降**である場合、この問題は既に修正済みであるため、影響はありません。

対処方法：
1.  **NFSボリュームの使用状況を確認：** まず、現在運用中のGKEクラスターがNFSボリュームをマウントして利用しているかを確認してください。
2.  **GKEクラスターのバージョンを確認：** NFSボリュームを使用している場合、現在のGKEクラスターのバージョンを確認してください。
3.  **バージョンが古い場合：** もしクラスターのバージョンが `1.34.1-gke.2877000` より古い場合は、計画的にクラスターを対象バージョン（またはそれ以降の推奨バージョン）にアップグレードすることを推奨します。これにより、2025年10月14日に発生する可能性があったNFSマウントの問題を回避できます。
4.  **リリースチャンネルの活用：** GKEのリリースチャンネル（Stable, Regularなど）を利用している場合は、通常、時間経過とともに自動的に推奨バージョンにアップグレードされるため、特別な手動対応は不要ですが、リリースチャンネルのバージョン進行状況は適宜確認してください。

用語説明：
*   **MountVolume:** Kubernetesにおいて、Podが外部ストレージまたは内部ストレージを自身のファイルシステムに接続（マウント）する操作を指します。これにより、Pod内のコンテナがそのボリュームにアクセスできるようになります。
*   **NFS (Network File System):** ネットワークを介してファイルシステムを共有するための分散ファイルシステムプロトコルです。Kubernetesでは、NFSサーバー上に存在するディレクトリをPersistentVolumeとして定義し、Podから利用することができます。
*   **GKEバージョン:** Google Kubernetes Engineのクラスターが稼働しているKubernetesのバージョンと、Google Cloudが独自に提供するパッチや機能が含まれたバージョン識別子です。`1.34.1-gke.2877000` のような形式で表記されます。