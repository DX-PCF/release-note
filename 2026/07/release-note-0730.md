
# Title: July 28, 2026 
Link: https://docs.cloud.google.com/release-notes#July_28_2026<br>
Google Cloud のリリースノートに対するお問い合わせありがとうございます。

現在、提供されているリリースノートの原文は「# Cloud SDK - Breaking」というカテゴリ名のみで、具体的な変更内容が記載されておりません。そのため、詳細な影響調査を行うことができません。

つきましては、お手数ですが、具体的なリリースノートの原文をご提示いただけますでしょうか。原文をご提示いただければ、以下のフォーマットに沿って影響調査を実施し、ご回答いたします。

---

**（以下は、仮にリリースノートの具体的な内容が提供された場合に想定される、一般的な `Cloud SDK` の `Breaking Change` に対する回答の枠組みです。具体的な内容は、リリースノート原文に依存します。）**

# Cloud SDK

## Breaking

**原文:**
[ここに提供されるリリースノートの原文を記載します]

**説明:**
**（具体的なリリースノートの内容に基づいて、日本語で分かりやすく説明します）**
例：このリリースでは、`gcloud CLI` の特定のコマンド（例：`gcloud compute instances create`）において、既存のフラグ（例：`--zone`）の動作が変更された、または特定のAPI（例：`projects.locations.deployments`）のレスポンス形式に非互換な変更が加えられました。これにより、旧バージョンで動作していたスクリプトや自動化ツールが、新しいSDKバージョンではエラーになる可能性があります。

**影響有無:**
**（具体的なリリースノートの内容と、貴社環境でのCloud SDKの使用状況に基づいて判断します）**
*   **影響あり**
    *   **理由:** 貴社環境では `Cloud SDK` の `gcloud CLI` コマンドや関連ライブラリが、CI/CDパイプライン、運用スクリプト、ローカル開発環境で広く利用されています。特に、既存の自動化スクリプトやツールが、今回の `Breaking Change` の影響を受ける可能性のあるコマンドやAPIを使用している場合、SDKのバージョンアップにより機能しなくなる恐れがあります。
    *   利用されている Google Cloud Composer (Composer version 2.7.1、Airflow version 2.7.3) のDAG内で `gcloud CLI` コマンドを直接呼び出している場合、Composerインスタンスが利用するCloud SDKのバージョンが変更された際に影響を受ける可能性があります。

*   **影響なし**
    *   **理由:** （例：貴社環境では当該変更が影響する特定の `gcloud CLI` コマンドやAPIを使用していない、または `Cloud SDK` を使用するサービス自体がデプロイされていないため、直接的な影響はありません。）

**対処方法:**
**（具体的なリリースノートの内容と、影響有無に基づいて対処方法を提案します）**
*   `Cloud SDK` のバージョンアップを行う前に、十分な事前検証を実施してください。特に、影響を受ける可能性のあるスクリプト、CI/CDパイプライン、Airflow DAGなどを対象に、テスト環境での動作確認を推奨します。
*   `gcloud CLI` コマンドや利用しているSDKライブラリのバージョンを固定している場合は、影響を受けるAPI/コマンドの変更点に合わせてスクリプトやコードを修正してください。
*   公式ドキュメントや移行ガイド（リリースノートにリンクがあれば）を参照し、推奨される新しい記述方法や代替手段に移行してください。
*   `Cloud Composer` をご利用の場合、Composerが内部で利用するCloud SDKのバージョンはGoogleによって管理されますが、ユーザーがAirflow DAG内で利用する `gcloud CLI` コマンドが今回の変更の影響を受ける可能性があります。ComposerインスタンスのCloud SDKバージョンが更新される前に、該当するDAGの動作確認および必要に応じた修正を検討してください。

**用語説明:**
*   **Cloud SDK:** Google Cloud のサービスをコマンドラインから操作したり、プログラマブルにアクセスしたりするためのツールキット群です。これには `gcloud CLI`（コマンドラインインターフェース）、`gsutil`（Cloud Storage用ツール）、`bq`（BigQuery用ツール）などが含まれます。
*   **Breaking Change（非互換な変更）:** ソフトウェアやAPIの変更において、既存のバージョンとの互換性が失われる変更のことです。これにより、アップデート後に既存のコードや設定が正しく動作しなくなる可能性があります。
*   **gcloud CLI:** Cloud SDK の主要なコンポーネントであり、Google Cloud の様々なサービスを管理するための統一されたコマンドラインツールです。
*   **Cloud Composer:** Google Cloud が提供する、マネージドな Apache Airflow サービスです。ワークフローの定義、スケジューリング、モニタリングを簡単に行えます。Airflow DAG（Directed Acyclic Graph）内で `gcloud CLI` コマンドを実行するタスクを定義することが可能です。
# Title: July 27, 2026 
Link: https://docs.cloud.google.com/release-notes#July_27_2026<br>
はい、承知いたしました。
Google Cloudのリリースノートについて、製品ごとの影響調査結果を専門的な言葉遣いと書式で回答します。

---

# Apigee X

## Announcement

**原文:** On July 27th, 2026, we released an updated version of Apigee (1-18-0-apigee-2).

> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

**説明:** Apigeeの新バージョン `1-18-0-apigee-2` がリリースされました。このロールアウトは既に開始されており、全てのGoogle Cloudゾーンでの完了には4営業日以上かかる可能性があります。そのため、お客様のApigeeインスタンスに新機能や修正が反映されるまでには、若干のタイムラグが生じる可能性があります。

**影響有無:**
*   **影響あり (間接的):** Apigee Xはマネージドサービスであるため、お客様のインスタンスは自動的にこの新バージョンに更新されます。これにより、後述のセキュリティ修正やバグ修正が適用され、サービスの安定性およびセキュリティ体制が向上します。明示的なお客様側での操作は不要です。

**対処方法:**
*   お客様側での具体的な対処は不要です。Google Cloudによる自動アップデートが適用されるため、ロールアウト完了を待つことで、新機能および修正が利用可能になります。

---

## Security

| Bug ID | Description |
| --- | --- |
| **534852923** | **Security fix for Apigee.** Fixed a security issue in the Java Callout policy. |

**説明:** ApigeeのJava Calloutポリシーにおけるセキュリティ脆弱性が修正されました。

**影響有無:**
*   **影響あり (ポジティブ):** Apigee Xをご利用のお客様で、特にJava Calloutポリシーを実装している場合、この修正により既存のデプロイメントのセキュリティが強化されます。悪用される可能性のある脆弱性が解消されるため、サービス全体のセキュリティ体制が向上します。

**対処方法:**
*   Apigee Xはマネージドサービスであるため、お客様側での直接的な対処（例: パッチ適用、バージョンアップ）は不要です。Google Cloudによって自動的に修正が適用されます。

---

## Security

| Bug ID | Description |
| --- | --- |
| **N/A** | **Security fix for Apigee infrastructure.** |

**説明:** Apigeeの基盤インフラストラクチャにおけるセキュリティ脆弱性が修正されました。

**影響有無:**
*   **影響あり (ポジティブ):** Apigee Xをご利用の全てのお客様に対して、基盤となるインフラストラクチャのセキュリティが強化されます。これにより、サービス全体の堅牢性と信頼性が向上します。

**対処方法:**
*   Apigee Xはマネージドサービスであるため、お客様側での直接的な対処は不要です。Google Cloudによって自動的に修正が適用されます。

---

## Fixed

| Bug ID | Description |
| --- | --- |
| **N/A** | Updates to infrastructure and libraries. |

**説明:** Apigeeの基盤インフラストラクチャおよび利用されている内部ライブラリが更新されました。

**影響有無:**
*   **影響あり (ポジティブ):** Apigee Xの基盤が最新の状態に保たれることで、パフォーマンスの向上、安定性の向上、および将来の機能拡張への対応といった間接的なメリットが期待されます。

**対処方法:**
*   Apigee Xはマネージドサービスであるため、お客様側での直接的な対処は不要です。Google Cloudによって自動的に更新が適用されます。

---

# BigQuery

## Change

**原文:** The feature formerly known as the *legacy `tabledata.insertAll` method* is now
called the *Storage Write API (REST)*. The feature formerly known as the *Storage Write API* is now called the *Storage Write API (gRPC)*.

[*Storage Write API (REST)*](https://docs.cloud.google.com/bigquery/docs/streaming-data-into-bigquery)
[*Storage Write API (gRPC)*](https://docs.cloud.google.com/bigquery/docs/write-api)

**説明:** BigQueryにおけるデータ書き込みAPIの名称が変更されました。
*   以前の「レガシーな `tabledata.insertAll` メソッド」は、「Storage Write API (REST)」という名称に変更されました。これは主にHTTP RESTfulインターフェースを介してBigQueryにデータをストリーミングするためのものです。
*   以前の「Storage Write API」は、「Storage Write API (gRPC)」という名称に変更されました。これはgRPCインターフェースを介してBigQueryにデータを書き込むための、より高性能で堅牢なAPIです。

**影響有無:**
*   **影響なし (名称変更のみ):** この変更は、既存のAPI機能や動作に影響を与えるものではなく、単なる名称の変更です。APIの機能性、呼び出し方法、料金体系に変更はありません。既存のアプリケーションやスクリプトは、引き続き変更なく動作します。

**対処方法:**
*   既存のコードや設定に対する変更は不要です。
*   今後、BigQueryのデータ取り込みに関するドキュメントを参照したり、新しい開発を行う際には、新しいAPI名称（`Storage Write API (REST)` または `Storage Write API (gRPC)`）を使用することで、より正確な情報を得られるでしょう。

**用語説明:**
*   **`tabledata.insertAll`:** BigQueryにリアルタイムでデータをストリーミングするための従来のAPIです。現在では、より高機能なStorage Write APIの使用が推奨されています。
*   **Storage Write API:** BigQueryに大量のデータを効率的かつ堅牢に書き込むためのAPIです。
    *   **REST (Representational State Transfer):** HTTPプロトコルをベースとしたWebサービス設計スタイルで、Webブラウザや汎用HTTPクライアントからのアクセスに適しています。
    *   **gRPC (gRPC Remote Procedure Calls):** Googleが開発した高性能なオープンソースRPCフレームワークです。HTTP/2を基盤とし、Protocol Buffersによる効率的なシリアライズにより、低レイテンシで高スループットな通信を可能にします。マイクロサービス間通信やリアルタイムデータ処理に特に適しています。

---

# Google Kubernetes Engine

## Security

**原文:** The general availability (GA) stage of mixed-protocol Services of type LoadBalancer fixes errors in traffic routing from stages prior to GA. This feature is in the GA stage in GKE version 1.36.2-gke.1498000 and later.

**説明:** GKEにおける`LoadBalancer`タイプのサービスで、TCPとUDPなど複数のプロトコルを同時に提供できる「混合プロトコルサービス」が一般提供 (GA) となりました。このGAバージョンでは、プレGA段階で存在したトラフィックルーティングに関するエラーが修正されています。この機能はGKEバージョン `1.36.2-gke.1498000` 以降でGAとして利用可能です。

**影響有無:**
*   **影響あり (ポジティブ):**
    *   GKEバージョン `1.36.2-gke.1498000` 以降のクラスターをご利用の場合、この機能はGAとして利用可能となり、以前のトラフィックルーティングの問題が解消されます。
    *   もし、これまで`LoadBalancer`サービスでTCPとUDPなどの混合プロトコルを使用しており、トラフィックルーティングの不安定さに直面していた場合、このGAリリースにより問題が解決し、より安定した運用が可能になります。
    *   異なるプロトコル（例: TCPとUDP）を同一のLoadBalancer Serviceを介して提供する必要があるワークロードにとって、この修正は安定性と信頼性を向上させます。

**対処方法:**
*   現在GKEバージョン `1.36.2-gke.1498000` より古いバージョンを使用しており、この「混合プロトコルサービス」の安定性を活用したい場合は、GKEクラスターのバージョンアップを検討してください。
*   既存の`LoadBalancer`タイプのサービスに対して、設定変更は基本的に不要です。この修正は基盤レベルの改善であり、アプリケーションやサービス定義に直接的な非互換性はありません。

**用語説明:**
*   **General Availability (GA):** 一般提供。Google Cloudの製品や機能が安定版として公式にリリースされ、本番環境での利用が推奨される段階です。品質、スケーラビリティ、サポート体制が確保されています。
*   **Service (Kubernetes):** KubernetesにおけるServiceは、Podのセットに対する安定したネットワークアクセスを抽象化するリソースです。内部ネットワーク内でのサービスディスカバリや、外部からのロードバランシングを提供します。
*   **LoadBalancer (Service Type):** Kubernetes Serviceのタイプの一つで、クラウドプロバイダ（Google Cloudの場合、Cloud Load Balancing）の外部ロードバランサーをプロビジョニングし、Kubernetesクラスター内のPodに外部からのトラフィックをルーティングします。
*   **Mixed-protocol Services:** 単一のKubernetes `Service`に対して、異なるIPプロトコル（例: TCPとUDP）のポートを混在させて公開する機能です。これにより、単一のロードバランサーでTCPとUDPの両方のトラフィックを処理できるようになります。