
# Title: July 28, 2026 
Link: https://docs.cloud.google.com/release-notes#July_28_2026<br>
リリースノートの原文が提供されていません。

恐れ入りますが、`# Cloud SDK ## Breaking` のセクションに続く**具体的なリリースノートの原文（英語）**をご提供ください。原文をいただければ、その内容に基づいて、ご要望の形式で影響調査を行います。
# Title: July 27, 2026 
Link: https://docs.cloud.google.com/release-notes#July_27_2026<br>
Google Cloudのリリースノートに関する影響調査結果を以下にまとめます。

---

# Apigee X

## Announcement

**原文:**
On July 27th, 2026, we released an updated version of Apigee (1-18-0-apigee-2).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

**説明:**
Apigeeの新しいバージョン `1-18-0-apigee-2` が2026年7月27日にリリースされました。このバージョンの展開（ロールアウト）は現在進行中で、すべてのGoogle Cloudゾーンで完了するまでに4営業日以上かかる可能性があります。そのため、お客様のApigeeインスタンスに新しい機能や修正が適用されるまでには時間差が生じる場合があります。

**影響有無:**
*   **影響あり（間接的）:** 新しいバージョンがリリースされ、後述のセキュリティ修正やバグ修正が含まれているため、より堅牢で安全な環境が提供されることになります。これはマネージドサービスであるため、Google側で自動的に適用されますが、反映されるまでのタイムラグが発生します。
*   **理由:** ApigeeはGoogle Cloudが提供するフルマネージドサービスであり、バージョンアップや修正の適用はGoogle側で自動的に行われます。ユーザー側での直接的な操作は不要ですが、リリースが完了するまでの間、最新の修正が適用されていない状態となる可能性があります。

**対処方法:**
特段の対処は不要です。リリースが完了するまで、Apigeeインスタンスが最新の機能や修正を利用できない可能性があることを認識しておいてください。もし本番環境のサービス稼働に影響を与える可能性がある場合は、Apigeeのサービス状況を適宜モニタリングすることをお勧めします。

**用語説明:**
*   **Apigee:** Google Cloudが提供するAPIライフサイクル管理プラットフォーム。APIの設計、開発、公開、運用、分析などを統合的にサポートします。
*   **ロールアウト:** ソフトウェアやサービスの新しいバージョンを、すべてのユーザーやシステムに段階的に展開していくプロセス。

## Security

**原文:**

| Bug ID | Description |
| --- | --- |
| **534852923** | **Security fix for Apigee.** Fixed a security issue in the Java Callout policy. |
| **N/A** | **Security fix for Apigee infrastructure.** |

**説明:**
Apigeeのセキュリティに関する2つの修正が適用されました。
1.  **Java Calloutポリシーにおけるセキュリティ修正:** ApigeeのJava Calloutポリシーに存在していたセキュリティ上の問題が修正されました。
2.  **Apigeeインフラストラクチャにおけるセキュリティ修正:** Apigeeの基盤となるインフラストラクチャにおけるセキュリティ上の問題が修正されました。

**影響有無:**
*   **影響あり（ポジティブ）:** 既存のApigeeサービスにおいてセキュリティ上の脆弱性が解消され、より安全にサービスを運用できるようになります。
*   **理由:** これらの修正はApigeeのマネージドサービスとしてGoogle側で自動的に適用されるため、ユーザー側のシステムやアプリケーションの動作に直接的な影響はありません。セキュリティ体制の強化に繋がります。

**対処方法:**
特段の対処は不要です。自動的に修正が適用されることでセキュリティが強化されます。

**用語説明:**
*   **Java Callout policy:** ApigeeのAPIプロキシフロー内で、カスタムのJavaコードを実行できるようにするポリシー。APIのロジックを柔軟に拡張するために使用されます。
*   **インフラストラクチャ:** サービスを稼働させるための基盤となるハードウェア、ソフトウェア、ネットワークなどの構成要素。

## Fixed

**原文:**

| Bug ID | Description |
| --- | --- |
| **N/A** | Updates to infrastructure and libraries. |

**説明:**
Apigeeの基盤インフラストラクチャと、使用されているライブラリが更新されました。

**影響有無:**
*   **影響なし（ポジティブな影響の可能性あり）:** これらの更新は、システムの安定性、パフォーマンス、またはセキュリティの向上を目的としている可能性があります。既存のApigeeサービスの動作に直接的な変更や停止を引き起こすものではありません。
*   **理由:** Apigeeはマネージドサービスであるため、基盤インフラストラクチャやライブラリの更新はGoogle側で自動的に行われます。ユーザー側での対応は不要です。

**対処方法:**
特段の対処は不要です。

**用語説明:**
*   **ライブラリ:** プログラムの特定の機能を提供するために、あらかじめ用意されたコードの集合体。

---

# BigQuery

## Change

**原文:**
The feature formerly known as the *legacy `tabledata.insertAll` method* is now called the *Storage Write API (REST)*. The feature formerly known as the *Storage Write API* is now called the *Storage Write API (gRPC)*.

[*Storage Write API (REST)*](https://docs.cloud.google.com/bigquery/docs/streaming-data-into-bigquery)
[*Storage Write API (gRPC)*](https://docs.cloud.google.com/bigquery/docs/write-api)

**説明:**
BigQueryへのデータ書き込みに関するAPIの名称が変更されました。
*   これまでの「レガシーな `tabledata.insertAll` メソッド」は「**Storage Write API (REST)**」と呼称されるようになりました。
*   これまでの「Storage Write API」は「**Storage Write API (gRPC)**」と呼称されるようになりました。
これは機能そのものの変更ではなく、あくまでAPIの名称変更であり、既存のAPIの動作には影響ありません。

**影響有無:**
*   **影響なし:** これは機能の名称変更であり、既存のAPI呼び出しやスクリプト、アプリケーションの動作に影響はありません。
*   **理由:** リリースノートに「formerly known as（以前は〜として知られていた）」と明記されており、機能そのものに変更があったわけではなく、呼称の整理が目的であることが示唆されています。

**対処方法:**
特段の対処は不要です。今後、BigQueryのドキュメントを参照したり、新しい開発を行う際には、新しいAPI名で言及するようにしてください。既存のコードを変更する必要はありません。

**用語説明:**
*   **BigQuery:** Google Cloudが提供する、ペタバイト規模のデータを超高速で分析できるフルマネージドのエンタープライズデータウェアハウス。
*   **`tabledata.insertAll`:** BigQueryにデータをストリーミング挿入するためのAPIメソッド。レガシーなメソッドとして扱われています。
*   **Storage Write API:** BigQueryに大量のデータを効率的に書き込むために推奨されるAPI。高スループットと低レイテンシを実現します。
*   **REST (Representational State Transfer):** Webサービス設計の原則に基づくアーキテクチャスタイルで、HTTPプロトコルを介してリソースを操作します。
*   **gRPC (gRPC Remote Procedure Call):** Googleが開発したオープンソースの高性能RPCフレームワーク。HTTP/2をベースにしており、多言語をサポートします。

---

# Google Kubernetes Engine

## Security

**原文:**
The general availability (GA) stage of mixed-protocol Services of type LoadBalancer fixes errors in traffic routing from stages prior to GA. This feature is in the GA stage in GKE version 1.36.2-gke.1498000 and later.

**説明:**
Google Kubernetes Engine (GKE) において、`LoadBalancer`タイプのサービスで「mixed-protocol Services」（複数の異なるプロトコルを混在させるサービス）がGeneral Availability (GA) ステージに移行しました。このGA移行に伴い、GA前の段階で存在していたトラフィックルーティングに関するエラーが修正されています。この機能はGKEバージョン `1.36.2-gke.1498000` 以降でGAとして提供されます。

**影響有無:**
*   **影響あり（ポジティブ）:** もし現在、GKEクラスタで`LoadBalancer`タイプのmixed-protocol Servicesを利用している場合、トラフィックルーティングの安定性が向上し、これまでの潜在的な問題が解決される可能性があります。
*   **理由:** この変更は、既存機能の安定化と改善を目的としており、特に特定のGKEバージョン（`1.36.2-gke.1498000` 以降）でGAとなるため、該当バージョン以上のクラスタを使用している場合は自動的にこの恩恵を受けることができます。

**対処方法:**
*   もし利用中のGKEクラスタのバージョンが `1.36.2-gke.1498000` 未満である場合、この修正の恩恵を受けるためには、クラスタのアップグレードを検討してください。
*   現在、`LoadBalancer`タイプのmixed-protocol Servicesを利用していて、過去にトラフィックルーティングに関する問題に遭遇していた場合は、今回の修正で問題が解決される可能性があります。

**用語説明:**
*   **Google Kubernetes Engine (GKE):** Google Cloudが提供する、コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを自動化するフルマネージドKubernetesサービス。
*   **General Availability (GA):** ソフトウェアやサービスが、本番環境での利用が推奨される安定した状態に達したことを示す開発段階。
*   **LoadBalancer Service:** KubernetesのServiceタイプの1つで、外部からのトラフィックをGKEクラスタ内のPodにルーティングするために、クラウドプロバイダのロードバランサをプロビジョニングします。
*   **Mixed-protocol Services:** 単一のKubernetes Service定義内で、TCPとUDPなど、異なるネットワークプロトコルのポートを同時に公開する機能。
*   **トラフィックルーティング:** ネットワーク上のデータパケットが、送信元から目的地へと進む経路を決定し、転送するプロセス。