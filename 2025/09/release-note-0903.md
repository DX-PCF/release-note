
# Title: September 02, 2025 
Link: https://cloud.google.com/release-notes#September_02_2025<br>
Google Cloud のインフラエンジニアとして、リリースノートに基づき、構築済みのサービスへの影響を調査し、簡潔に回答します。

---

# Cloud Service Mesh
## Fixed
原文: 1.26.4-asm.1 is now available for in-cluster Cloud Service Mesh. This patch release contains a fix for a use-after-free (UAF) vulnerability in the DNS cache. For more information, see the security bulletin. Only clusters running in-cluster Cloud Service Mesh version 1.26 are affected. If you are running an earlier in-cluster version or managed Cloud Service Mesh, you are not affected and do not need to take any action. For details on upgrading Cloud Service Mesh, refer to Upgrade Cloud Service Mesh.

説明:
Cloud Service Mesh の `in-cluster` 版向けに、バージョン `1.26.4-asm.1` がリリースされました。このパッチリリースには、DNSキャッシュにおける Use-After-Free (UAF) のセキュリティ脆弱性 (CVE-2025-54588) の修正が含まれています。
この脆弱性の影響を受けるのは、`in-cluster Cloud Service Mesh version 1.26` を実行しているクラスタのみです。それ以前の `in-cluster` バージョンや、`managed Cloud Service Mesh` を利用している場合は影響を受けず、特別な対応は不要です。

影響有無:
**利用状況による影響あり**
現在ご利用中の環境で **`in-cluster Cloud Service Mesh version 1.26` を使用している場合、この脆弱性の影響を受ける可能性があります。**
ただし、ご指定の「Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)」は直接 Cloud Service Mesh とは関連がありません。Cloud Service Mesh は通常、Google Kubernetes Engine (GKE) 上でサービスメッシュを構築する際に利用されます。
もし GKE クラスタで `in-cluster Cloud Service Mesh version 1.26` を利用されている場合は、影響があると判断されます。それ以外のバージョンまたは `managed Cloud Service Mesh` を利用している場合、あるいは Cloud Service Mesh を利用していない場合は影響はありません。

対処方法:
ご自身の環境で **`in-cluster Cloud Service Mesh version 1.26` をご利用中の場合は、速やかに `1.26.4-asm.1` へのアップグレードを強く推奨します。**
アップグレードの詳細については、以下の公式ドキュメントを参照してください。

*   [Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/docs/upgrade/upgrade)

用語説明:
*   **in-cluster Cloud Service Mesh**: Google Kubernetes Engine (GKE) クラスタの内部に直接コンポーネントをデプロイし、ユーザー自身で管理する形式の Cloud Service Mesh です。これに対し、Googleがコンポーネントの管理を行う `managed Cloud Service Mesh` があります。
*   **use-after-free (UAF) vulnerability**: 解放済みのメモリ領域をプログラムが誤って再利用しようとすることで発生するセキュリティ脆弱性です。これにより、意図しないコード実行や情報漏洩につながる可能性があります。
*   **DNS cache**: ドメイン名システム (DNS) の解決結果を一時的に保存しておく場所です。これにより、同じドメイン名の問い合わせに対して、再度DNSサーバーにアクセスすることなく高速に応答できます。
*   **patch release**: 主にバグ修正やセキュリティ脆弱性の修正など、小規模な変更を含むソフトウェアリリースです。
*   **security bulletin**: 製品やサービスにおけるセキュリティ関連の脆弱性や脅威、それらへの対策について公式に発表される情報です。
# Title: September 01, 2025 
Link: https://cloud.google.com/release-notes#September_01_2025<br>
はい、承知いたしました。Google Cloud BigQueryのリリースノートについて、製品への影響有無を調査し、ご提示いただいた形式で回答いたします。

---

# BigQuery

## Changed

### Go Client Library Updates (bigquery/storage/apiv1beta1)

**原文:**
- **bigquery/reservation:** Add Reservation.max_slots field to Reservation proto, indicating the total max number of slots this reservation can use up to (f1de706)
- **bigquery/reservation:** Add Reservation.scaling_mode field and its corresponding enum message ScalingMode. This field should be used together with Reservation.max_slots (f1de706)
- **bigquery/storage/managedwriter:** Allow overriding proto conversion mapping (#12579) (ce9d29b), refs #12578
- **bigquery:** Add load/extract job completion ratio (#12471) (3dab483)
- **bigquery:** Load job and external table opts for custom time format, null markers and source column match (#12470) (67b0320)

**説明:**
Google Cloud Goクライアントライブラリの `bigquery/storage/apiv1beta1` および関連コンポーネントがバージョン 1.70.0 へ更新されました。この更新には以下の主要な機能追加と改善が含まれます。

*   **BigQuery 予約の機能強化**: BigQueryの予約（Reservation）管理において、予約が使用できるスロットの総量を指定する `max_slots` フィールドと、スケーリング挙動を制御する `scaling_mode` フィールド（関連する `ScalingMode` enum と併用）が追加されました。
*   **BigQuery Storage Write APIの柔軟性向上**: ManagedWriterを通じてデータを書き込む際に、Protocol Buffers（Proto）の変換マッピングをオーバーライドできるようになりました。これにより、データ取り込み時の柔軟な変換制御が可能になります。
*   **ロード/抽出ジョブの監視機能強化**: BigQueryのロードジョブおよび抽出ジョブの進捗状況を示す「完了率（`completion ratio`）」が追加され、ジョブの実行状況の可視性が向上しました。
*   **ロードジョブおよび外部テーブルのオプション追加**: データロードと外部テーブル定義において、カスタム時間形式、NULLマーカー、ソースカラムとターゲットカラムのマッチング方法を指定する新たなオプションが追加され、多様なデータフォーマットへの対応とインポート処理の柔軟性が向上しました。

**影響有無:**
**影響なし（ポジティブな影響あり）**
これらの変更はGoクライアントライブラリにおける機能追加および改善であり、既存の機能に対する破壊的な変更（Breaking Change）は含まれていません。そのため、現在のシステム構成やアプリケーションの動作に直接的な悪影響はありません。
むしろ、BigQueryの予約管理の高度化、データロードの柔軟性、およびジョブの監視機能の強化といった新しい機能が利用可能になるため、将来的なシステム拡張や運用効率の向上に寄与する可能性があります。

**対処方法:**
特別な対処は不要です。
もし、上記の新機能を利用したい場合や、最新のGoクライアントライブラリのバグ修正やパフォーマンス改善を取り込みたい場合は、Goアプリケーションの依存関係を最新バージョン（1.70.0以降）に更新してください。

**用語説明:**
*   **BigQuery Reservation (BigQuery 予約)**: BigQueryのオンデマンド課金モデルとは異なり、専用のクエリ処理能力（スロット）を一定期間予約して利用する料金モデルです。ワークロードのパフォーマンスを安定させ、コストを予測可能にする目的で利用されます。
*   **スロット (Slots)**: BigQueryがクエリを実行するために使用する、仮想CPUのようなコンピューティング能力の単位です。
*   **BigQuery Storage Write API**: BigQueryに大量のデータを高速かつ低レイテンシでストリーミング書き込みするためのAPIです。バッチ処理だけでなくリアルタイムに近いデータ取り込みが求められるシナリオで利用されます。
*   **ManagedWriter**: BigQuery Storage Write APIの一部として提供されるクライアントサイドのユーティリティで、データ書き込みの並行処理やエラーハンドリングなどを抽象化し、開発者が容易にストリーミング書き込みを行えるようにします。
*   **Protocol Buffers (Proto)**: Googleが開発した、構造化データを効率的にシリアライズ（直列化）するための言語に依存しないデータ形式です。データ通信やデータ永続化に広く利用されます。

---

### Java Client Library Update (google-cloud-bigquery)

**原文:**
- Update dependency com.google.cloud:sdk-platform-java-config to v3.52.0 (#3939) (794bf83)

**説明:**
Google Cloud Javaクライアントライブラリの `google-cloud-bigquery` がバージョン 2.54.2 へ更新されました。この更新は、内部的な依存関係である `com.google.cloud:sdk-platform-java-config` のバージョンを `v3.52.0` に更新するものです。

**影響有無:**
**影響なし**
この変更は、Javaクライアントライブラリの内部的な依存関係のバージョンアップであり、BigQuery APIの利用に直接影響を与えるような機能変更や動作変更を伴いません。既存のアプリケーションの動作には影響はありません。

**対処方法:**
特別な対処は不要です。
最新のバグ修正やパフォーマンス改善、またはその他のセキュリティアップデートを取り込みたい場合は、JavaアプリケーションのMavenやGradleなどの依存関係管理ツールを使用して `google-cloud-bigquery` ライブラリを最新バージョン（2.54.2以降）に更新してください。

**用語説明:**
*   **依存関係 (Dependency)**: あるソフトウェアモジュールやライブラリが適切に機能するために必要とする、他のソフトウェアコンポーネントやライブラリのことです。
*   **Maven/Gradle**: Javaプロジェクトで広く利用されるビルド自動化ツールおよび依存関係管理ツールです。プロジェクトのコンパイル、テスト、パッケージング、デプロイなどのプロセスを自動化します。

---