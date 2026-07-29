
# Title: July 27, 2026 
Link: https://docs.cloud.google.com/release-notes#July_27_2026<br>
Google Cloudのリリースノートに対する調査結果を以下に報告します。

---

# Apigee X

## Announcement

**原文:**
On July 27th, 2026, we released an updated version of Apigee (1-18-0-apigee-2).

> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

**説明:**
Apigeeの新バージョン `1-18-0-apigee-2` がリリースされました。このリリースの展開（ロールアウト）は本日開始されており、全てのGoogle Cloudゾーンに適用が完了するまでに4営業日以上かかる可能性があります。ロールアウトが完了するまでは、新しい機能や修正がお客様のインスタンスで利用できない場合があります。

**影響有無:**
影響あり。ApigeeはGoogle Cloudが管理するサービスであるため、今回のバージョンアップは自動的に適用されます。これにより、後述のセキュリティ修正やバグ修正が環境に導入されます。ロールアウト期間中は、特定の機能や修正が一時的に利用できない、または環境間でバージョンが異なる可能性があります。

**対処方法:**
特にユーザー側で直接的な対応は不要です。ApigeeのバージョンはGoogle Cloudによって管理されます。今回のリリースに含まれるセキュリティ修正やバグ修正の適用状況を把握し、サービス運用への影響がないか監視を継続してください。ロールアウト完了後に、変更が意図通り適用されたことを確認することが推奨されます。

**用語説明:**
*   **Rollout:** ソフトウェアやサービスの新しいバージョンを、影響を最小限に抑えながら段階的にデプロイしていくプロセスです。

## Security

**原文:**
| Bug ID | Description |
| --- | --- |
| **534852923** | **Security fix for Apigee.** Fixed a security issue in the Java Callout policy. |
| **N/A** | **Security fix for Apigee infrastructure.** |

**説明:**
*   ApigeeのJava Calloutポリシーにおけるセキュリティ上の脆弱性が修正されました。
*   Apigeeの基盤となるインフラストラクチャに関するセキュリティ修正が行われました。

**影響有無:**
影響あり。Apigeeのプラットフォーム全体のセキュリティが向上します。Java Calloutポリシーを利用している場合、セキュリティ強化により潜在的なリスクが低減されます。

**対処方法:**
特段のユーザー側の対応は不要です。これらのセキュリティ修正は、上記のAnnouncementで述べられたバージョンアップの一部として自動的に適用されます。Java Calloutポリシーを使用している場合は、念のため修正適用後に期待する動作に影響がないか確認することを推奨しますが、通常はポジティブな影響のみです。

**用語説明:**
*   **Java Callout policy:** ApigeeのAPIプロキシ内で、複雑なビジネスロジックや外部サービスとの連携のためにカスタムのJavaコードを実行させるポリシーです。

## Fixed

**原文:**
| Bug ID | Description |
| --- | --- |
| **N/A** | Updates to infrastructure and libraries. |

**説明:**
Apigeeの基盤となるインフラストラクチャおよび使用されているライブラリが更新されました。

**影響有無:**
影響なし。インフラストラクチャとライブラリの更新は、サービスの安定性、パフォーマンス、セキュリティの向上を目的としており、通常、直接的な機能変更や非互換性は発生しません。

**対処方法:**
特にユーザー側の対応は不要です。

**用語説明:**
*   **Libraries:** ソフトウェア開発において、特定の機能を提供する再利用可能なコードの集合体です。セキュリティパッチの適用やパフォーマンス改善のために更新されることがあります。

---

# BigQuery

## Change

**原文:**
The feature formerly known as the *legacy `tabledata.insertAll` method* is now
called the
*Storage Write API (REST)*. The
feature formerly known as the *Storage Write API* is now called the
*Storage Write API (gRPC)*.

[*Storage Write API (REST)*](https://docs.cloud.google.com/bigquery/docs/streaming-data-into-bigquery)
[*Storage Write API (gRPC)*](https://docs.cloud.google.com/bigquery/docs/write-api)

**説明:**
BigQueryへのデータ書き込みに関連するAPIの名称が変更されました。
*   これまでの「レガシーな `tabledata.insertAll` メソッド」は「Storage Write API (REST)」に名称変更されました。
*   これまでの「Storage Write API」は「Storage Write API (gRPC)」に名称変更されました。
これは機能そのものの変更ではなく、ドキュメントにおける用語の明確化を目的とした名称変更です。

**影響有無:**
影響なし。既存のアプリケーションやスクリプトの動作に影響はありません。機能の変更ではなく、あくまで名称の変更です。

**対処方法:**
特段の対応は不要です。今後は新しい名称でのドキュメント参照や、社内外でのコミュニケーション時に新しい名称を使用することが推奨されます。

**用語説明:**
*   **`tabledata.insertAll` (Legacy):** BigQueryの古いストリーミング挿入APIで、リクエストごとに少量のデータを挿入するのに適しています。
*   **Storage Write API:** BigQueryにストリーミングで大量のデータを書き込むための推奨APIです。高スループットと信頼性の高いデータ挿入が可能です。
*   **REST (Representational State Transfer):** Webサービスの設計原則の一つで、HTTPプロトコルをベースにしています。
*   **gRPC (Google Remote Procedure Call):** Googleが開発したオープンソースの高性能RPCフレームワークで、HTTP/2をベースに高速な通信を可能にします。

---

# Google Kubernetes Engine

## Security

**原文:**
The general availability (GA) stage of mixed-protocol Services of type
LoadBalancer fixes errors in traffic routing from stages prior to GA. This
feature is in the GA stage in GKE version 1.36.2-gke.1498000 and later.

**説明:**
GKEのLoadBalancerタイプのサービスにおいて、異なるプロトコルを混在させて使用できる「Mixed-protocol Services」が正式リリース版（General Availability: GA）となりました。このGA化により、GA以前のバージョンで存在していたトラフィックルーティングに関するエラーが修正されます。この機能はGKEバージョン `1.36.2-gke.1498000` 以降でGAとして提供されます。

**影響有無:**
影響あり。
*   現在、LoadBalancerタイプのサービスでTCP/UDPなど複数のプロトコルを混在して使用しており、トラフィックルーティングの問題が発生していた場合は、GKEクラスターを対象バージョン以上にアップグレードすることで問題が解決されます。
*   GKEクラスターのバージョンが `1.36.2-gke.1498000` 未満の場合、今後のクラスターアップグレードによりこの修正が自動的に適用され、当該機能の安定性と信頼性が向上します。

**対処方法:**
*   現在使用しているGKEクラスターのバージョンが `1.36.2-gke.1498000` 未満である場合は、この修正の恩恵を受けるためにクラスターのアップグレードを検討してください。
*   LoadBalancerタイプのサービスで混合プロトコルを使用している場合は、アップグレード後にトラフィックルーティングが意図通りに行われていることを確認してください。

**用語説明:**
*   **General Availability (GA):** ソフトウェアや機能が正式にリリースされ、本番環境での使用が推奨される段階です。安定性、信頼性、サポート体制が保証されます。
*   **Mixed-protocol Services:** KubernetesのServiceオブジェクトで、異なるネットワークプロトコル（例: TCPとUDP）を同じサービス内で処理できるように設定されたものです。
*   **LoadBalancer Service:** KubernetesのServiceタイプの一つで、クラウドプロバイダのロードバランサーをプロビジョニングし、クラスタ外部からのトラフィックをService内のPodに分散させる役割を担います。