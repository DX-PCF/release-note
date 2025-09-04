
# Title: September 02, 2025 
Link: https://cloud.google.com/release-notes#September_02_2025<br>
Google Cloud のインフラエンジニアとして、リリースノートに基づき、構築済みのサービスへの影響調査結果を以下に報告します。

---

# Cloud Service Mesh

## Security
原文:
```
 1.26.4-asm.1 is now available for in-cluster Cloud Service Mesh.

 This patch release contains a fix for a use-after-free (UAF) vulnerability in the DNS cache. For more information, see the security bulletin.

[use-after-free (UAF) vulnerability in the DNS cache](https://www.cve.org/CVERecord?id=CVE-2025-54588)
[security bulletin](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2025-048)
 Only clusters running in-cluster Cloud Service Mesh version 1.26 are affected. If you are running an earlier in-cluster version or managed Cloud Service Mesh, you are not affected and do not need to take any action.

 For details on upgrading Cloud Service Mesh, refer to Upgrade Cloud Service Mesh.

[Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/docs/upgrade/upgrade)
```
説明:
in-cluster Cloud Service Mesh のバージョン `1.26.4-asm.1` が新たにリリースされました。このパッチリリースには、DNSキャッシュにおける `use-after-free (UAF)` 脆弱性（CVE-2025-54588）の修正が含まれています。この脆弱性の影響を受けるのは、in-cluster Cloud Service Mesh のバージョン 1.26 を実行しているクラスターのみです。これ以前の in-cluster バージョン、または Managed Cloud Service Mesh を利用している場合は影響を受けません。

影響有無:
*   **もし in-cluster Cloud Service Mesh バージョン 1.26 をご利用の場合**: 影響があります。DNSキャッシュにセキュリティ脆弱性が存在するため、速やかなアップデートを推奨します。
*   **もし in-cluster Cloud Service Mesh バージョン 1.26 以外（以前のバージョン）または Managed Cloud Service Mesh をご利用の場合**: 影響はありません。特段の対応は不要です。

対処方法:
*   **in-cluster Cloud Service Mesh バージョン 1.26 をご利用の場合**:
    セキュリティ脆弱性の修正のため、対象のCloud Service Mesh インスタンスをバージョン `1.26.4-asm.1` へ速やかにアップグレードすることを強く推奨します。アップグレード手順については、[Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/docs/upgrade/upgrade) ドキュメントをご参照ください。
*   **上記以外の場合**: 特に対処は不要です。

用語説明:
*   **in-cluster Cloud Service Mesh**: Google Kubernetes Engine (GKE) クラスタ内にService Meshのコントロールプレーンとデータプレーンがデプロイされ、ユーザーがService Meshのライフサイクル（インストール、アップグレード、設定など）を管理するデプロイメントモデルです。
*   **Managed Cloud Service Mesh**: GoogleがService Meshのコントロールプレーンを管理し、ユーザーはデータプレーンであるサイドカープロキシのみをクラスタにデプロイするモデルです。Google Cloudのマネージドサービスとして提供されるため、運用負荷が軽減されます。
*   **Use-After-Free (UAF) 脆弱性**: プログラムがすでに解放（解放されたメモリはOSに返還される）されたメモリ領域を、意図せず再度使用しようとしたときに発生するセキュリティ脆弱性の一種です。この脆弱性を悪用されると、データの破損、サービス拒否 (DoS)、または任意のコード実行など、深刻なセキュリティリスクにつながる可能性があります。
*   **DNSキャッシュ**: Domain Name System (DNS) の解決結果を一時的に保存しておく仕組みです。これにより、同じドメイン名の再解決にかかる時間とネットワーク負荷を削減できます。

---

# Google Kubernetes Engine

## Announcement
原文:
```
 Features that were part of GKE Enterprise are now available as part of the standard GKE offering, or offered as standalone SKUs.

 The following advanced multi-cluster management and networking features are included in the GKE offering at no additional cost:

- Fleet dashboard
- Multi-team Management
- Config Sync
- Config Controller
- Managed Policy Controller
- Connect Gateway
- Network Function Optimizer
- Fully Qualified Domain Name (FQDN) Network Policy
- Inter-node Transparent Encryption

 The following GKE Enterprise features continue to be available using their current standalone SKUs. If you are using any of these features, your billing is automatically transitioned to the corresponding standalone SKU.

- Managed Cloud Service Mesh
- Multicluster Gateways; Multicluster Ingress
- Binary Authorization
- Advanced Vulnerability Scanning
- GKE Extended Support (LTS)
```
説明:
GKE Enterprise で提供されていた一部の高度な機能が、標準の GKE プランの一部として追加費用なしで利用可能になるか、または個別のスタンドアロン SKU として提供されるようになったというアナウンスです。

*   **GKE標準で追加費用なしで利用可能になる機能**:
    Fleet dashboard, Multi-team Management, Config Sync, Config Controller, Managed Policy Controller, Connect Gateway, Network Function Optimizer, Fully Qualified Domain Name (FQDN) Network Policy, Inter-node Transparent Encryption
    これらの機能は、既存の GKE 環境で利用できるようになります。
*   **既存のスタンドアロンSKUで引き続き利用可能となる機能（課金が自動移行）**:
    Managed Cloud Service Mesh, Multicluster Gateways; Multicluster Ingress, Binary Authorization, Advanced Vulnerability Scanning, GKE Extended Support (LTS)
    これらの機能を利用していた場合、既存の請求は自動的に対応するスタンドアロンSKUに移行されます。

影響有無:
*   **GKE Enterprise の機能を現在ご利用の場合**:
    *   **標準GKEに無償で含まれるようになった機能を利用していた場合**: 費用面でのメリットが発生します。これらの機能は今後、GKEの通常利用料金の範囲内で利用できるようになります。
    *   **スタンドアロンSKUに移行する機能を利用していた場合**: 機能の利用方法自体に影響はありませんが、請求モデルが変更されます。Google側で請求が自動的に新しいSKUに移行されるため、ユーザー側での手動移行作業は不要です。既存の契約や割引が新しいSKUにどのように適用されるかについては、課金部門と確認することが推奨されます。
*   **GKE Enterprise の機能を現在ご利用ではない場合**:
    直接的な影響はほとんどありません。ただし、これまでGKE Enterpriseを利用しなければ利用できなかった高度なマルチクラスター管理やネットワーキング機能が、標準GKEで手軽に利用できるようになるため、今後のアーキテクチャ設計や運用改善の選択肢が広がります。
    （注: Google Cloud Composer2 はGKE上で動作しますが、本変更はGKEクラスタ自体および利用される付加機能に関するものであり、Composerの動作に直接的な影響はありません。ただし、ComposerがデプロイされているGKEクラスタで、上記GKE Enterpriseの機能を別途利用している場合は、その機能についての影響を受けます。）

対処方法:
*   **GKE Enterprise の機能を現在ご利用の場合**:
    ユーザー側での設定変更などの直接的な対処は不要です。Google側で請求の移行が行われます。課金の移行に伴い、コスト構造を確認したい場合は、Google CloudのBillingレポートをご確認ください。
    また、標準GKEに無償で含まれるようになった機能については、これを機に既存の運用改善や新規機能導入の機会として検討することをお勧めします。
*   **GKE Enterprise の機能を現在ご利用ではない場合**:
    特に対処は不要です。

用語説明:
*   **GKE Enterprise**: Google Kubernetes Engine (GKE) の上位エディションであり、高度なセキュリティ機能、マルチクラスター管理、ハイブリッドクラウド・マルチクラウド環境への拡張など、大規模なエンタープライズ環境向けに特化した機能を提供するサービスです。以前はAnthosの一部として提供されていました。
*   **SKU (Stock Keeping Unit)**: 在庫管理単位。Google Cloudにおいては、サービスの使用量やリソースに対して課金される最小単位を指します。
*   **Fleet dashboard**: 複数のGKEクラスタを論理的なグループ（フリート）として登録し、フリート内の全クラスタの状態を一元的に可視化・管理するためのダッシュボードです。
*   **Config Sync**: Gitリポジトリで定義されたKubernetesリソースの宣言的な構成（マニフェスト）を、フリート内のGKEクラスタに自動的に同期・適用する機能です。GitOpsワークフローをサポートします。
*   **Config Controller**: Google Cloud上でのKubernetesリソースやその他のGoogle Cloudリソース（例: Cloud SQLインスタンス、VPCネットワークなど）を一元的に宣言的に管理するための、Kubernetesベースのコントロールプレーンです。
*   **Managed Policy Controller**: Kubernetesクラスタにおけるセキュリティやコンプライアンスポリシーを集中管理し、ポリシー違反を検出・強制するための機能です。Open Policy Agent (OPA) Gatekeeper を基盤としています。
*   **Connect Gateway**: Anthos Connect を利用して、GKEクラスタを含むフリート内のクラスタと、Google Cloudのサービスとの間で、安全かつ効率的な通信パスを確立するための機能です。オンプレミスや他のクラウドプロバイダーに存在するクラスタとの接続も可能にします。
*   **Binary Authorization**: デプロイ時にコンテナイメージの署名を強制し、承認された（信頼できる）イメージのみがGKEクラスタにデプロイされるようにするセキュリティ機能です。これにより、サプライチェーン攻撃のリスクを軽減します。
# Title: September 01, 2025 
Link: https://cloud.google.com/release-notes#September_01_2025<br>
はい、承知いたしました。Google CloudのBigQueryに関するリリースノートについて、製品への影響調査を実施し、ご指定の形式で回答いたします。

---

# BigQuery

## Changed (Go Client Library Update)

原文:
- **bigquery/reservation:** Add Reservation.max_slots field to Reservation proto, indicating the total max number of slots this reservation can use up to (f1de706)
- **bigquery/reservation:** Add Reservation.scaling_mode field and its corresponding enum message ScalingMode. This field should be used together with Reservation.max_slots (f1de706)
- **bigquery/storage/managedwriter:** Allow overriding proto conversion mapping (#12579) (ce9d29b), refs #12578
- **bigquery:** Add load/extract job completion ratio (#12471) (3dab483)
- **bigquery:** Load job and external table opts for custom time format, null markers and source column match (#12470) (67b0320)

説明：
Go言語向けBigQueryクライアントライブラリ (bigquery/storage/apiv1beta1) がバージョン 1.70.0 に更新されました。この更新には以下の機能追加が含まれます。

*   **BigQuery Reservations機能の拡張:**
    *   スロット予約設定に `Reservation.max_slots` フィールドが追加され、予約が利用できる最大スロット数を指定できるようになりました。
    *   スロット予約設定に `Reservation.scaling_mode` フィールドと対応する `ScalingMode` 列挙型が追加され、スロットのスケール方法（例えば、flex/autoscaleなど）を制御できるようになりました。これらは `max_slots` と組み合わせて使用します。
*   **BigQuery Storage Write API (ManagedWriter) の改善:**
    *   Protobuf形式のデータ変換マッピングをオーバーライドする機能が追加され、より柔軟なデータ書き込みが可能になりました。
*   **ジョブ監視機能の強化:**
    *   BigQueryのデータロードジョブおよびデータ抽出ジョブについて、完了率 (completion ratio) を取得する機能が追加されました。これにより、ジョブの進捗状況をより詳細に監視できるようになります。
*   **データロードおよび外部テーブル設定の柔軟性向上:**
    *   ロードジョブと外部テーブルのオプションに、カスタム時刻形式の指定、NULL値マーカー（特定の文字列をNULLとして扱う設定）、およびソースカラムとターゲットカラムの自動一致に関する設定が追加されました。これにより、様々な形式のデータをより容易にBigQueryにロードできるようになります。

影響有無：
**なし。**
これらの変更は、BigQueryのGoクライアントライブラリに新しい機能を追加するものであり、既存のAPIや機能の動作に非互換な変更（Breaking Change）は含まれていません。既存のBigQueryリソースやジョブの実行には直接的な影響はありません。
Google Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3) はPythonベースであり、Goクライアントライブラリを直接利用しているわけではないため、この変更による直接的な影響はありません。

対処方法：
**不要。**
現在これらの新機能を利用していない場合、特段の対処は必要ありません。
もし、上記の新機能（例：スロット予約の拡張機能、より詳細なジョブ進捗監視、柔軟なデータロードオプション）をGoアプリケーションで利用したい場合は、BigQuery Goクライアントライブラリを最新バージョン (1.70.0以降) に更新し、それに応じてコードを修正する必要があります。

用語説明：
*   **BigQuery Reservations:** BigQueryの計算リソースである「スロット」を事前に予約し、一定の料金で安定したクエリパフォーマンスを確保する仕組み。これにより、オンデマンド料金と比較して費用効率を高めたり、重要なワークロードに専用リソースを割り当てたりできます。
*   **BigQuery Storage Write API:** BigQueryにストリーミングデータやバッチデータを効率的に書き込むための高性能API。特に、ManagedWriterは、レコードバッファリングやエラー処理などをクライアント側で自動的に管理する機能を提供します。
*   **Protobuf (Protocol Buffers):** Googleが開発した、構造化データをシリアライズ（直列化）するための言語ニュートラル、プラットフォームニュートラル、拡張可能なメカニズム。APIやデータストレージでよく利用されます。

---

## Changed (Java Client Library Update)

原文:
- Update dependency com.google.cloud:sdk-platform-java-config to v3.52.0 (#3939) (794bf83)

説明：
Java言語向けBigQueryクライアントライブラリ (google-cloud-bigquery) がバージョン 2.54.2 に更新されました。この更新は、内部依存関係である `com.google.cloud:sdk-platform-java-config` のバージョンを 3.52.0 に引き上げたものです。これは、主に内部的なライブラリ構成や共通設定の更新であり、バグ修正や性能改善が含まれる可能性があります。

影響有無：
**なし。**
この変更は、BigQuery Javaクライアントライブラリが内部的に利用する共通の構成ライブラリのバージョンアップです。通常、このような依存関係の更新は、後方互換性を維持しつつ、安定性やパフォーマンスの向上、あるいはセキュリティの強化を目的として行われます。直接的な非互換性のある変更や、既存のAPIの動作に影響を与える可能性は極めて低いと考えられます。
Google Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3) はPythonベースであり、Javaクライアントライブラリを直接利用しているわけではないため、この変更による直接的な影響はありません。

対処方法：
**不要。**
既存のBigQuery Javaクライアントライブラリを利用しているアプリケーションで、特に問題が発生していない限り、特段の対処は必要ありません。安定性やパフォーマンスの改善といった恩恵を受けるために、計画的なライブラリのバージョンアップを検討することは推奨されます。

用語説明：
*   **依存関係 (Dependency):** ソフトウェア開発において、あるコンポーネントやライブラリが機能するために必要とする他のコンポーネントやライブラリのこと。
*   **sdk-platform-java-config:** Google Cloud Java SDK群全体で共通して利用される設定やユーティリティを提供する内部ライブラリ。