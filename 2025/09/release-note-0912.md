
# Title: September 10, 2025 
Link: https://cloud.google.com/release-notes#September_10_2025<br>
Google Cloudのインフラエンジニアとして、提供されたリリースノートに基づき、Cloud Service Meshに関する影響調査と推奨される対応を以下の通りご報告いたします。

---

# Cloud Service Mesh

## Announcement

原文: `1.26.4-asm.1 in-cluster Cloud Service Mesh already includes the fixes for these CVEs.`

説明:
インクラスター型のCloud Service Meshバージョン1.26.4-asm.1には、後述の「Fixed」セクションで詳細が説明される複数のCVE（共通脆弱性識別子）に対する修正がすでに含まれていることが発表されました。これは、このバージョンを使用しているユーザーは、これらのセキュリティ脆弱性から保護されていることを意味します。

影響有無:
*   **もしCloud Service Meshをインクラスターモードで利用しており、かつバージョン1.26.4-asm.1を使用している場合:** 影響はありません。対象となるセキュリティ修正はすでに適用されています。
*   **もしCloud Service Meshをインクラスターモードで利用しているが、バージョン1.26.4-asm.1未満の場合:** 影響があります。最新のセキュリティ修正が含まれていないため、脆弱性の影響を受ける可能性があります。

対処方法:
*   Cloud Service Meshをインクラスターモードで利用しており、かつバージョン1.26.4-asm.1未満の場合は、セキュリティリスクを軽減するため、最新の推奨バージョン（本リリースノートでは1.26.4-asm.1や、後述の1.25.4-asm.0、1.24.6-asm.12など）へのアップグレードを検討してください。

用語説明:
*   **インクラスター型Cloud Service Mesh:** Google Kubernetes Engine (GKE) クラスター内にコントロールプレーンとデータプレーンをデプロイし、GKEクラスター内でサービスメッシュ機能を提供するデプロイメントモデルです。

---

## Announcement

原文: `**1.25.4-asm.0 is now available for in-cluster Cloud Service Mesh.**
You can now download 1.25.4-asm.0 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.25.4 subject to the list of supported features. Cloud Service Mesh version 1.25.4-asm.0 uses envoy v1.33.8-dev.
[Istio 1.25.4](https://istio.io/latest/news/releases/1.25.x/announcing-1.25.4/)
[supported features](https://cloud.google.com/service-mesh/v1.25/docs/supported-features-in-cluster)
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh.
[Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/v1.25/docs/upgrade/upgrade)`

説明:
インクラスター型のCloud Service Meshバージョン1.25.4-asm.0が利用可能になったことが発表されました。このバージョンはIstio 1.25.4の機能に基づいており、特定のサポート対象機能リストに従います。また、データプレーンのプロキシとしてEnvoy v1.33.8-devを使用しています。Istio 1.25.4のリリースノートや、Cloud Service Meshのサポート機能、アップグレード手順へのリンクが提供されています。

影響有無:
*   **もしCloud Service Meshをインクラスターモードで利用している場合:** 影響があります。より新しいIstioの機能と、潜在的なセキュリティ修正（前のAnnouncementとFixedセクションに関連）を含む最新バージョンが利用可能になったため、アップグレードを検討する機会が提供されます。
*   **もしCloud Service Meshを利用していない場合:** 直接的な影響はありません。

対処方法:
*   Cloud Service Meshを利用している場合は、 Istio 1.25.4の機能の恩恵を受け、かつセキュリティを強化するために、このバージョンへのアップグレードを検討してください。アップグレード計画の際には、提供されているドキュメント「[Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/v1.25/docs/upgrade/upgrade)」を参照し、現在の環境との互換性やサポートされる機能を確認することが重要です。

用語説明:
*   **Istio:** マイクロサービスを接続、監視、保護するためのオープンソースのサービスメッシュプラットフォームです。Cloud Service MeshはIstioをベースにしています。
*   **Envoy:** 高性能なオープンソースのL7プロキシであり、サービスメッシュのデータプレーンとして広く利用されています。サービス間のトラフィックを処理します。

---

## Announcement

原文: `**1.24.6-asm.12 is now available for in-cluster Cloud Service Mesh.**
You can now download 1.24.6-asm.12 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.24.6 subject to the list of supported features. Cloud Service Mesh version 1.24.6-asm.12 uses envoy v1.33.8-dev.
[Istio 1.24.6](https://istio.io/latest/news/releases/1.24.x/announcing-1.24.6/)
[supported features](https://cloud.google.com/service-mesh/v1.24/docs/supported-features-in-cluster)
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh.
[Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/v1.24/docs/upgrade/upgrade)`

説明:
インクラスター型のCloud Service Meshバージョン1.24.6-asm.12が利用可能になったことが発表されました。このバージョンはIstio 1.24.6の機能に基づいており、特定のサポート対象機能リストに従います。Envoy v1.33.8-devをデータプレーンのプロキシとして使用しています。Istio 1.24.6のリリースノートや、Cloud Service Meshのサポート機能、アップグレード手順へのリンクが提供されています。

影響有無:
*   **もしCloud Service Meshをインクラスターモードで利用しており、Istio 1.24.6ベースのバージョンへのアップグレードを検討している場合:** 影響があります。このバージョンが利用可能になったことで、アップグレードの選択肢が提供されます。以前のバージョンからのセキュリティ修正（Fixedセクションに関連）や安定性の向上が期待されます。
*   **もしCloud Service Meshを利用していない場合:** 直接的な影響はありません。

対処方法:
*   Cloud Service Meshを利用しており、この特定のバージョンへのアップグレードが必要な場合や、より古いバージョンを使用している場合は、セキュリティや安定性向上のためにこのバージョンへのアップグレードを検討してください。アップグレード計画の際には、提供されているドキュメント「[Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/v1.24/docs/upgrade/upgrade)」を参照し、現在の環境との互換性やサポートされる機能を確認することが重要です。

---

## Fixed

原文: `These patches address the following CVEs:
| | | | | |
| CVE | Proxy | Control Plane | CNI | Distroless |
| CVE-2025-32990 | Yes | Yes | Yes | - |
| CVE-2025-32988 | Yes | Yes | Yes | - |
| CVE-2025-40909 | Yes | Yes | Yes | - |
| CVE-2025-32989 | Yes | Yes | Yes | - |
| CVE-2025-47268 | Yes | Yes | Yes | - |
| CVE-2025-5702 | Yes | Yes | Yes | - |
| CVE-2025-6395 | Yes | Yes | Yes | - |
| CVE-2025-48964 | Yes | Yes | Yes | - |
[CVE-2025-32990](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-32990)
[CVE-2025-32988](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-32988)
[CVE-2025-40909](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-40909)
[CVE-2025-32989](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-32989)
[CVE-2025-47268](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-47268)
[CVE-2025-5702](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-5702)
[CVE-2025-6395](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-6395)
[CVE-2025-48964](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-48964)`

説明:
このパッチリリースには、複数の重要なセキュリティ脆弱性（CVE）に対する修正が含まれています。これらのCVEは、Cloud Service MeshのProxy（Envoy）、Control Plane、およびCNIコンポーネントに影響を与える可能性がありました。これらの修正は、サービスメッシュのセキュリティ体制を強化し、潜在的な攻撃経路を塞ぐものです。

影響有無:
*   **もしCloud Service Meshをインクラスターモードで利用しており、これらのCVEの影響を受ける可能性のあるバージョンを使用している場合:** 影響があります。これらの脆弱性が修正されたため、アップグレードしない限り、システムは既知の脆弱性にさらされるリスクがあります。
*   **もしCloud Service Meshを最新の推奨バージョン（例えば1.26.4-asm.1）で利用している場合:** 影響はありません。修正はすでに含まれています。
*   **もしCloud Service Meshを利用していない場合:** 直接的な影響はありません。

対処方法:
*   Cloud Service Meshを利用している場合は、システムをこれらの既知の脆弱性から保護するために、修正が含まれる最新のCloud Service Meshバージョンへのアップグレードを強く推奨します。アップグレードの詳細は、上記の各Announcementセクションで提供されているアップグレードドキュメントを参照してください。

用語説明:
*   **CVE (Common Vulnerabilities and Exposures):** ソフトウェアやシステムのセキュリティ脆弱性を一意に識別するための共通識別子です。
*   **Proxy (プロキシ):** この文脈では主にEnvoyプロキシを指し、サービスメッシュ内でサービス間の通信を仲介し、トラフィックルーティング、負荷分散、セキュリティポリシー適用などを行います。
*   **Control Plane (コントロールプレーン):** サービスメッシュの管理層であり、ネットワークポリシー、トラフィックルーティングルール、オブザーバビリティ設定などを管理・適用します。Istioのコンポーネント（Pilot, Citadel, Galleyなど）が含まれます。
*   **CNI (Container Network Interface):** Kubernetesクラスター内でコンテナのネットワーク接続を構成するための仕様です。サービスメッシュのコンポーネント（例: Istio CNI）が、Podのネットワーク設定に介入し、トラフィックをサイドカープロキシにリダイレクトするために使用されます。
*   **Distroless:** 必要最小限のOSコンポーネントしか含まない、軽量でセキュアなコンテナイメージのことです。このリリースノートでは、特定のCVEがDistrolessイメージには影響しないことを示唆しています（ただし、この表ではDistrolessは対象外となっています）。
# Title: September 09, 2025 
Link: https://cloud.google.com/release-notes#September_09_2025<br>
承知いたしました。Google Cloudのリリースノートに基づき、構築済みのサービスへの影響有無を調査し、指定された形式で回答します。

---

# Apigee X
## Announcement
原文: On September 9, 2025, we released an updated version of Apigee (1-16-0-apigee-1).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明：Apigeeの新しいバージョン1-16-0-apigee-1が2025年9月9日にリリースされました。このリリースは現在各Google Cloudゾーンで順次展開中であり、完了までには4営業日以上かかる場合があります。この展開が完了するまでは、利用中のApigeeインスタンスで新機能や修正が利用できない可能性があります。

影響有無：影響なし。本リリースは新しいバージョンの展開に関するアナウンスであり、既存のサービス動作に直接的な影響を与えるものではありません。セキュリティインフラやライブラリの更新（後述）が含まれており、サービスの安定性とセキュリティが向上します。ただし、展開が完了するまで、このバージョンで導入された新機能や修正が利用できない期間が存在します。

対処方法：特になし。新機能の利用や特定の修正の適用を期待する場合は、ロールアウトの完了を待つ必要があります。自動的な更新のため、ユーザー側で特別な操作は不要です。

用語説明：
*   **Apigee X**: Google Cloudが提供するフルマネージドのAPI管理プラットフォームです。APIの設計、デプロイ、保護、監視、分析を一元的に行えます。
*   **Rollout**: ソフトウェアやシステムの新しいバージョンを段階的に展開していくプロセスを指します。これにより、変更による影響を最小限に抑えつつ、安定性を確保します。

## Changed
原文: | Bug ID | Description |
| --- | --- |
| **N/A** | **Updates to security infrastructure and libraries.** |

説明：Apigeeの基盤となるセキュリティインフラストラクチャおよび使用されるライブラリが更新されました。

影響有無：影響なし。本変更は、Apigeeの内部的なセキュリティ強化と維持管理に関連するものであり、既存のAPIプロキシやアプリケーションの動作に直接的な変更や非互換性は発生しません。サービスのセキュリティ体勢が向上します。

対処方法：特になし。

---

# BigQuery
## Changed
原文: You can now perform supervised tuning on a BigQuery ML remote model based on a Vertex AI `gemini-2.5-pro` or `gemini-2.5-flash-lite` model.
[supervised tuning](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model#supervised_tuning)
[remote model](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model)

説明：BigQuery MLの機能が拡張され、Vertex AIの`gemini-2.5-pro`または`gemini-2.5-flash-lite`モデルに基づいたリモートモデルに対して、教師ありチューニングを実行できるようになりました。

影響有無：影響なし。この変更は新機能の追加であり、既存のBigQuery MLの挙動やデータパイプラインに影響を与えるものではありません。BigQuery MLで外部LLMモデルを活用している、または今後活用を検討しているユーザーにとって、モデル性能向上に寄与する新たなオプションが提供されます。

対処方法：特になし。必要に応じて、新しい教師ありチューニング機能の利用を検討し、関連ドキュメント（[supervised tuning](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model#supervised_tuning)、[remote model](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model)）を参照して導入を計画してください。

用語説明：
*   **BigQuery ML**: BigQuery内で機械学習モデルを作成・実行できる機能です。SQL構文を用いて、大規模なデータセットに対してモデルトレーニングや推論を行うことができます。
*   **Remote model (リモートモデル)**: BigQuery MLの機能の一つで、BigQueryの外部にある機械学習モデル（この場合はVertex AIのGeminiモデル）をBigQueryから呼び出して利用できるようにするものです。
*   **Supervised tuning (教師ありチューニング)**: 特定のタスクやデータセットに合わせて、事前に用意されたラベル付きデータ（教師データ）を使ってモデルのパラメータを微調整（ファインチューニング）するプロセスです。これにより、モデルのパフォーマンスを向上させることができます。
*   **Vertex AI**: Google Cloudが提供する機械学習プラットフォームで、データ準備、モデルの構築、トレーニング、デプロイ、監視など、機械学習のライフサイクル全体をサポートします。
*   **Gemini 2.5 Pro / Flash Lite**: Googleが開発した大規模言語モデル（LLM）のシリーズです。Proは高性能モデル、Flash Liteはより高速で軽量なモデルを指します。

---

# Cloud Service Mesh
## Security
原文: The managed Cloud Service Mesh rollouts previously announced address the following vulnerabilities. While the managed data plane automatically updates Envoy Proxies by restarting workloads, you must manually restart any StatefulSets and Jobs.
[previously announced](https://cloud.google.com/service-mesh/docs/release-notes#August_12_2025)
**1.21.5-asm.55**, **1.20.8-asm.48**, **1.19.10-asm.48** (詳細なCVEリストは省略)

説明：マネージドCloud Service Meshのロールアウトにより、複数のセキュリティ脆弱性（CVE）が修正されました。マネージドデータプレーンはワークロードの再起動を通じてEnvoyプロキシを自動的に更新しますが、`StatefulSets`および`Jobs`については手動での再起動が必要です。

影響有無：影響あり。Cloud Service Meshを利用している環境では、セキュリティ脆弱性が修正されセキュリティ体勢が向上します。しかし、`StatefulSets`または`Jobs`タイプのワークロードを使用している場合、手動での再起動が必要となり、これによって一時的なサービス停止が発生する可能性があります。弊社環境でCloud Service Meshが利用されているかどうか、および`StatefulSets`や`Jobs`がデプロイされているかを確認する必要があります。Google Cloud Composer2はマネージドサービスであるため、基盤となるGKEクラスターにおけるCloud Service Meshの管理はGoogle側で行われることが一般的ですが、Composer環境内で明示的にCloud Service Meshが有効化され、かつStatefulSetsやJobsがAirflow DAGsなどによってデプロイされている場合は、この影響を考慮する必要があります。

対処方法：
1.  **Cloud Service Meshの利用状況確認**: 現在のGoogle Cloud環境でCloud Service Meshが有効になっているかを確認します。
2.  **ワークロードタイプ確認**: Cloud Service Meshを利用しているKubernetesクラスタ内で、`StatefulSets`または`Jobs`タイプのワークロードが稼働しているかを確認します。
3.  **計画的な再起動**: `StatefulSets`または`Jobs`が稼働している場合、影響を受ける可能性のあるアプリケーションのダウンタイムを最小限に抑えるため、計画的なメンテナンス期間中にこれらのワークロードを手動で再起動します。再起動前に、対象ワークロードが停止しても問題ないことを確認し、必要な手順を策定してください。
4.  **CVEの内容確認**: リストされている各CVE（例: CVE-2025-32462, CVE-2025-4877など）の詳細を、提供されているリンクやCVEデータベースで確認し、自社環境への潜在的なリスクを評価します。

用語説明：
*   **Cloud Service Mesh**: Google Kubernetes Engine (GKE) 上で、サービス間の通信を管理・制御するGoogle Cloudのフルマネージドサービスメッシュソリューションです。Istioを基盤としています。
*   **Envoy Proxy**: マイクロサービスアーキテクチャで広く利用される、高性能なオープンソースのエッジ/サービスプロキシです。サービスメッシュのデータプレーンとして機能し、トラフィックルーティング、負荷分散、監視、セキュリティなどの機能を提供します。
*   **StatefulSets**: KubernetesのワークロードAPIオブジェクトの一つで、永続的なストレージや固定ネットワークIDを持つアプリケーション（例: データベースなど）のデプロイとスケーリングを管理するために使用されます。ポッドが再起動されてもその状態が維持される特性があります。
*   **Jobs**: KubernetesのワークロードAPIオブジェクトの一つで、指定されたタスクを1回だけ実行し、完了したら終了するタイプのポッドを管理するために使用されます。バッチ処理などに利用されます。
*   **CVE (Common Vulnerabilities and Exposures)**: 公開されているソフトウェアの脆弱性を一意に識別するための共通識別子です。

---

# Compute Engine
## Changed
原文: Hyperdisk Balanced High Availability disks are available in all regions. Hyperdisk Balanced High Availability disks synchronously replicate disk data from one zone to another. Cross-zonal replication provides data protection in the unlikely event of a zonal outage. For more information, see About Hyperdisk Balanced High Availability.
[About Hyperdisk Balanced High Availability](https://cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha)

説明：Compute EngineのHyperdisk Balanced High Availabilityディスクが、すべてのGoogle Cloudリージョンで利用可能になりました。このディスクタイプは、ディスクデータをあるゾーンから別のゾーンへ同期的にレプリケートし、ゾーン障害が発生した場合でもデータ保護を提供します。

影響有無：影響なし。これはCompute Engineにおける新しいディスクタイプの可用性向上に関するアナウンスであり、既存のディスク構成や仮想マシンの動作に影響を与えるものではありません。より高い耐障害性が求められるワークロードに対して、ストレージの選択肢が増えます。

対処方法：特になし。既存のディスクタイプからの移行は強制されません。将来的に、特定のワークロードでより高い可用性と耐障害性が必要となった際に、このHyperdisk Balanced High Availabilityの利用を検討してください。詳細については、提供されているドキュメント([About Hyperdisk Balanced High Availability](https://cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha))を参照してください。

用語説明：
*   **Compute Engine**: Google Cloudが提供する、仮想マシン（VM）インスタンスを実行できるインフラストラクチャサービスです。
*   **Hyperdisk Balanced High Availability (HA)**: Compute Engineが提供する高性能なブロックストレージディスクタイプの一つです。特に高いI/Oパフォーマンスと可用性を両立させるように設計されており、ゾーン障害からの回復力を高めるためにゾーン間での同期レプリケーションが可能です。
*   **Synchronous Replication (同期レプリケーション)**: データを複数の場所に同時に書き込むことで、書き込み処理が完了した時点で全てのレプリカが同期されていることを保証するデータ複製方式です。これにより、障害発生時でもデータの損失を最小限に抑えることができますが、書き込みレイテンシが増加する可能性があります。
*   **Zonal Outage (ゾーン障害)**: 特定のGoogle Cloudのゾーン全体が、何らかの理由（電力障害、ネットワーク障害など）で利用不能になる事態を指します。複数のゾーンにリソースを分散配置することで、ゾーン障害に対する耐障害性を高めることができます。

---
# Title: September 08, 2025 
Link: https://cloud.google.com/release-notes#September_08_2025<br>
はい、承知いたしました。Google Cloudのリリースノートを元に、Cloud LoggingおよびPub/Subに関する変更について、製品への影響有無と対処方法を調査し、専門的な言葉遣いと書式設定で回答します。

---

# Cloud Logging

## Fixed

原文:
```
Changes for @google-cloud/logging
[@google-cloud/logging](https://github.com/googleapis/nodejs-logging)
[11.2.1](https://github.com/googleapis/nodejs-logging/compare/v11.2.0...v11.2.1)
- **logging:** Specifying resourceNames should fetch logs only from those resources (#1597) (ff7899f)

[#1597](https://github.com/googleapis/nodejs-logging/issues/1597)
[ff7899f](https://github.com/googleapis/nodejs-logging/commit/ff7899f5e91da6540d3f68476b2d9acd58ff0993)
```

説明:
Node.js 用の Cloud Logging クライアントライブラリ `@google-cloud/logging` のバージョン `11.2.1` がリリースされました。このバージョンでは、ログの取得時に `resourceNames` パラメータを指定した場合、**指定されたリソースからのログのみを正確にフェッチする**ように修正されました。これは、以前のバージョンで `resourceNames` が意図した通りに機能せず、関連のないログも含まれてしまう可能性があったバグに対する修正です。

影響有無:
**影響あり（改善）**:
`resourceNames` を使用して特定のGoogle Cloudリソースからのログのみをフィルタリングして取得している Node.js アプリケーションにとって、ログ取得の精度が向上します。以前のバージョンでフィルタリングが不正確であった場合、この修正によって期待される挙動が実現されます。これは機能的な改善であり、Breaking Changeではありません。

理由:
この修正は、`resourceNames` によるログフィルタリングの正確性を向上させるものです。もし既存のアプリケーションがこの機能を利用している場合、本アップデートにより、より適切に意図したログのみを取得できるようになります。意図しないログが取得されていた環境では、ログ処理量やストレージ容量の削減につながる可能性もあります。

対処方法:
Node.js アプリケーションで `@google-cloud/logging` ライブラリを使用しており、`resourceNames` を用いたログフィルタリングを実装している場合は、このバージョン `11.2.1` 以降へのアップデートを推奨します。特に、`resourceNames` によるログフィルタリングの挙動に不整合を感じていた場合は、アップデートによって問題が解消される可能性があります。アップデートは `npm install @google-cloud/logging@latest` などで行えます。

用語説明:
*   `@google-cloud/logging`: Google Cloud Logging サービスと連携するためのNode.jsクライアントライブラリです。アプリケーションからログを書き込んだり、既存のログをクエリしたりするために使用されます。
*   `resourceNames`: Cloud Logging API でログを取得する際に、ログの発生源となる特定のGoogle Cloudリソース（例: `projects/my-project/locations/global/buckets/my-bucket` のようなログバケットや `projects/my-project/locations/global/resources/compute.googleapis.com/instances/my-vm` のようなVMインスタンス）に限定してログを取得したい場合に、そのリソースの完全なパスを指定するパラメータです。

---

# Pub/Sub

## Fixed / Changed

原文:
```
Changes for pubsub/apiv1

[pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)
[2.0.1](https://github.com/googleapis/google-cloud-go/compare/pubsub/v2/v2.0.0...pubsub/v2/v2.0.1)
- **pubsub/v2:** Update flowcontrol metrics even when disabled (#12590) (c153495)

[#12590](https://github.com/googleapis/google-cloud-go/issues/12590)
[c153495](https://github.com/googleapis/google-cloud-go/commit/c1534952c4a6c3a52dd9e3aab295d27d4107016c)
- **pubsub/v2:** Move wiki to package doc (#12605) (3de795e)

[#12605](https://github.com/googleapis/google-cloud-go/issues/12605)
[3de795e](https://github.com/googleapis/google-cloud-go/commit/3de795ecaf1782df76d9ac49499988369601d334)
[1.50.1](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.50.0...pubsub/v1.50.1)
- **pubsub/v2:** Update flowcontrol metrics even when disabled (#12590) (c153495)

[#12590](https://github.com/googleapis/google-cloud-go/issues/12590)
[c153495](https://github.com/googleapis/google-cloud-go/commit/c1534952c4a6c3a52dd9e3aab295d27d4107016c)
- **pubsub:** Update migration docs with seek (#12642) (40538c3)

[#12642](https://github.com/googleapis/google-cloud-go/issues/12642)
[40538c3](https://github.com/googleapis/google-cloud-go/commit/40538c3a8cbbd9a54deb6cdb204809d487aef21b)
```

説明:
Go言語用のGoogle Cloud Pub/Subクライアントライブラリ `pubsub/apiv1` のバージョン `2.0.1`（v2系）と `1.50.1`（v1系）がリリースされました。

主な変更点は以下の通りです:
*   **両バージョン共通**: Pub/Subの購読者（Subscriber）におけるフローコントロールメトリクスが、機能が無効化されている状態でも適切に更新されるように修正されました。これにより、クライアントの内部状態に関するメトリクスの正確性が向上します。
*   **v2.0.1 固有の変更**: ライブラリのWiki形式のドキュメントがパッケージドキュメント内に統合・移動されました。これはドキュメントの整理であり、機能的な変更ではありません。
*   **v1.50.1 固有の変更**: Pub/Subの `Seek` 機能に関するマイグレーションドキュメントが更新されました。これもドキュメントの改善であり、機能的な変更ではありません。

影響有無:
**影響なし**:
これらの変更は、主にGoクライアントライブラリの内部的な挙動の改善、メトリクスの正確性向上、およびドキュメントの整理に関するものです。既存のGoアプリケーションの機能的な動作に直接的な影響を与える非互換性の変更（Breaking Change）は含まれていません。

理由:
*   フローコントロールメトリクスの改善は、内部的な監視やデバッグの正確性を高めるものであり、アプリケーションのメッセージ処理ロジックや振る舞いを変更するものではありません。
*   ドキュメントの移動やマイグレーションガイドの更新は、情報提供の改善であり、Goコードのコンパイルや実行時の動作に影響を与えるものではありません。

対処方法:
Go言語でPub/Subクライアントライブラリを使用している場合、より正確なフローコントロールメトリクスや最新のドキュメントにアクセスするために、これらの更新を含む最新バージョン（v2系であれば `2.0.1` 以降、v1系であれば `1.50.1` 以降）へのアップデートを検討することは推奨されますが、必須ではありません。既存のアプリケーションコードの修正は通常不要です。

用語説明:
*   `pubsub/apiv1`: Google Cloud Pub/Subサービスと連携するためのGo言語クライアントライブラリです。メッセージの発行（Publish）や購読（Subscribe）を行うために使用されます。
*   フローコントロール（Flow Control）: Pub/Subの購読者（Subscriber）が一度に処理するメッセージの量（メッセージ数やバイト数）を制御する仕組みです。これにより、アプリケーションが処理能力を超過するメッセージを受け取らないようにし、リソースの枯渇やパフォーマンス低下を防ぎます。
*   メトリクス（Metrics）: システムやアプリケーションのパフォーマンス、状態、使用状況などを数値化した指標のことです。これらは監視ツールやダッシュボードで利用され、システムの健全性を把握するのに役立ちます。
*   Seek機能: Pub/Subの購読者（Subscriber）が、特定の時点や特定のスナップショットに購読の状態を巻き戻したり、進めたりする機能です。これにより、過去のメッセージを再処理したり、エラー発生時に特定のポイントから再開したりすることが可能になります。