
# Title: October 27, 2026 
Link: https://docs.cloud.google.com/release-notes#October_27_2026<br>
Google Cloudインフラエンジニアとして、ご依頼のリリースノートについて調査し、製品毎の影響有無、対処方法をまとめました。

---

# AlloyDB for PostgreSQL

## Announcement
原文:
The following AlloyDB AI functions and improvements are available in Preview:

[Preview](https://cloud.google.com/products#product-launch-stages)
- The `ai.extract` function lets you extract structured data from unstructured text directly within your database queries without needing external extraction pipelines. For more information, see Extract structured data.
- The `ai.classify` function lets you categorize unstructured text into predefined labels directly within your database queries. For more information, see Classify text.
- Parameter names and signatures for AI query engine functions (`ai.analyze_sentiment`, `ai.summarize`, and `ai.agg_summarize`) are updated. For more information, see Model endpoint reference.

- The `prompt` and `prompts` parameters are renamed to `input` and `inputs` in scalar and batch functions respectively.
- An optional `additional_instructions` parameter is added to `ai.summarize` and `ai.agg_summarize` to provide custom instructions to guide summary formatting, length, and tone.
- In cursor-based versions of `ai.analyze_sentiment` and `ai.summarize`, the `prompt` parameter is removed.
- `ai.agg_summarize` supports multiple positional signatures, including passing optional additional instructions and specifying model IDs.

The `ai.extract` function lets you extract structured data from unstructured text directly within your database queries without needing external extraction pipelines. For more information, see Extract structured data.

[Extract structured data](https://docs.cloud.google.com/alloydb/docs/ai/extract-structured-data)
The `ai.classify` function lets you categorize unstructured text into predefined labels directly within your database queries. For more information, see Classify text.

[Classify text](https://docs.cloud.com/alloydb/docs/ai/classify-text)
Parameter names and signatures for AI query engine functions (`ai.analyze_sentiment`, `ai.summarize`, and `ai.agg_summarize`) are updated. For more information, see Model endpoint reference.

[Model endpoint reference](https://docs.cloud.google.com/alloydb/docs/reference/model-endpoint)
- The `prompt` and `prompts` parameters are renamed to `input` and `inputs` in scalar and batch functions respectively.
- An optional `additional_instructions` parameter is added to `ai.summarize` and `ai.agg_summarize` to provide custom instructions to guide summary formatting, length, and tone.
- In cursor-based versions of `ai.analyze_sentiment` and `ai.summarize`, the `prompt` parameter is removed.
- `ai.agg_summarize` supports multiple positional signatures, including passing optional additional instructions and specifying model IDs.

The `prompt` and `prompts` parameters are renamed to `input` and `inputs` in scalar and batch functions respectively.

An optional `additional_instructions` parameter is added to `ai.summarize` and `ai.agg_summarize` to provide custom instructions to guide summary formatting, length, and tone.

In cursor-based versions of `ai.analyze_sentiment` and `ai.summarize`, the `prompt` parameter is removed.

`ai.agg_summarize` supports multiple positional signatures, including passing optional additional instructions and specifying model IDs.

説明：
AlloyDB for PostgreSQLのAI機能がプレビュー版として強化されました。
1.  **新機能の追加**:
    *   `ai.extract`: 非構造化テキストから構造化データを直接データベースクエリ内で抽出できます。
    *   `ai.classify`: 非構造化テキストを定義済みラベルに直接データベースクエリ内で分類できます。
2.  **既存AIクエリエンジン関数のパラメータとシグネチャの更新**:
    *   `ai.analyze_sentiment`、`ai.summarize`、`ai.agg_summarize` のパラメータが変更されました。
    *   `prompt`および`prompts`パラメータが`input`および`inputs`にそれぞれリネームされました。
    *   `ai.summarize`および`ai.agg_summarize`に、要約のフォーマット、長さ、トーンを指示するためのオプションの`additional_instructions`パラメータが追加されました。
    *   カーソルベースの`ai.analyze_sentiment`および`ai.summarize`から`prompt`パラメータが削除されました。
    *   `ai.agg_summarize`が、オプションの追加指示やモデルID指定を含む複数の位置シグネチャをサポートするようになりました。

影響有無：
**影響あり。**
既存のAIクエリエンジン関数を現在AlloyDB for PostgreSQL上で利用している場合、パラメータ名やシグネチャの変更により、関連するクエリやアプリケーションコードの修正が必要となります。特に`prompt`から`input`へのパラメータ名変更は互換性に影響します。新機能(`ai.extract`, `ai.classify`)の追加自体は、既存のサービスには直接的な影響はありません。

対処方法：
1.  現在AlloyDB for PostgreSQLのAIクエリエンジン関数（`ai.analyze_sentiment`, `ai.summarize`, `ai.agg_summarize`）を利用しているか確認します。
2.  利用している場合、公式ドキュメント「Model endpoint reference」を参照し、新しいパラメータ名とシグネチャに合わせて、アプリケーションやスクリプト内のSQLクエリを修正してください。
3.  新機能の利用を検討する場合は、ドキュメントを参照し、要件に合わせて実装してください。

用語説明：
*   **AlloyDB for PostgreSQL**: Google Cloudが提供するマネージドなPostgreSQL互換データベースサービスで、特にトランザクションと分析ワークロードの両方で高いパフォーマンスと可用性を提供します。
*   **AI Query Engine Functions**: AlloyDB内で直接実行できる機械学習機能を指します。これにより、データ抽出、テキスト分類、感情分析、テキスト要約などのAI/MLタスクをデータベースのSQLクエリから直接実行できます。
*   **Preview**: Google Cloudにおける製品のリリースステージの一つで、一般公開（GA）前の段階です。この段階の機能は、APIの変更や互換性のない変更が含まれる可能性があり、本番環境での利用は注意が必要です。
*   **シグネチャ (Signature)**: プログラミングにおいて、関数やメソッドの引数の型、数、順序、および戻り値の型を定義するものです。SQL関数においては、関数の名前と引数の組み合わせを指します。
*   **スカラー関数 (Scalar Function)**: 単一の入力値に対して単一の出力値を返す関数。
*   **バッチ関数 (Batch Function)**: 複数の入力値（通常は配列やテーブル）に対して複数の出力値を返す関数。

---

# Cloud DNS

## Announcement
原文:
Starting January 5, 2027, CNAME chasing behavior will change so that Cloud DNS follows CNAME chains between public and private zones. If your private zones or response policies have overlapping domain names with public CNAME targets, queries might resolve to unintended internal IP addresses or return resolution errors.

The following table outlines the current and updated behaviors.

| Source of CNAME answer | Current behavior (until January 5, 2027) | New behavior (starting January 5, 2027) |
| --- | --- | --- |
| Cloud DNS public zone | Subsequent queries search only public DNS zones and internal DNS. Private zones, forwarding zones, and response policies are ignored. | Subsequent queries follow the complete VPC name resolution order: response policies, private zones, forwarding or peering zones, internal DNS, and public zones. |
| Cloud DNS private zone | Subsequent queries search only authorized private zones. Public DNS zones are ignored. | Subsequent queries follow the complete VPC name resolution order. If the target isn't found in authorized private zones, Cloud DNS queries public DNS zones. |
| Cloud DNS response policy zone | Cloud DNS systems don't perform queries for CNAME answers received from response policy local data rules. | Subsequent queries follow the complete VPC name resolution order. If the target isn't found in response policies or private zones, Cloud DNS queries public DNS zones. |
Review your CNAME chasing needs before January 5, 2027. Test your DNS query paths using `dig` or `nslookup` to identify CNAME chasing scenarios.

- **Look for private-to-public CNAME chasing scenarios**: Look for CNAME answers from response policies or private zones that don't match any response policy or record in a private zone. Previously, these queries resulted in a `NXDOMAIN` answer but after January 5, 2027, these scenarios might match a record in a public zone or continue to be `NXDOMAIN` responses.
- **Look for public-to-private CNAME chasing scenarios**: Look for CNAME answers from public zones that don't match any record in a public zone. Previously, these CNAME chasing scenarios would have resulted in a `NXDOMAIN` response. After January 5, 2027, these scenarios might match a response policy or record in a private zone or continue to be `NXDOMAIN` responses if the private zone doesn't have the record.
- **For CNAME chasing scenarios under your control**: As best practice, configure matching time-to-live (TTL) values for all records in the CNAME chain.

説明：
2027年1月5日より、Cloud DNSのCNAMEチェイシング（CNAME解決の挙動）が変更されます。現在の挙動ではパブリックゾーンとプライベートゾーンの間でCNAMEチェイシングは行われませんが、変更後は完全なVPC名前解決順序に従い、両ゾーン間でのCNAME解決が行われるようになります。この変更により、プライベートゾーンやレスポンスポリシーに、パブリックCNAMEターゲットと重複するドメイン名がある場合、DNSクエリが意図しない内部IPアドレスに解決されたり、解決エラーが発生する可能性があります。

影響有無：
**影響あり。**
これは将来的な変更（2027年1月5日以降）ですが、既存のシステムがCloud DNSのCNAMEレコードをパブリックゾーンとプライベートゾーン、またはレスポンスポリシーをまたいで利用している場合、または重複するドメイン名を持つCNAMEが存在する場合に、重大な影響を及ぼす可能性があります。具体的には、誤ったIPアドレスへのルーティング、サービス停止、情報漏洩などのリスクが生じる可能性があります。

対処方法：
2027年1月5日までに、以下の手順で現在のDNS設定と挙動を確認し、必要に応じて修正してください。
1.  `dig`や`nslookup`などのツールを使用して、既存のCNAMEチェイシングシナリオを特定します。特に、プライベートゾーン/レスポンスポリシーからパブリックゾーンへのCNAME参照、およびパブリックゾーンからプライベートゾーン/レスポンスポリシーへのCNAME参照を確認します。
2.  CNAMEチェーン内の全てのレコードのTTL (Time-To-Live) 値を一致させることを検討してください。
3.  テスト環境で変更後の挙動をシミュレーションし、意図しない解決が発生しないか検証します。
4.  必要に応じて、CNAMEレコードの構成を見直し、ドメイン名の重複を避けるか、変更後のCNAMEチェイシング挙動に合わせた設計に変更します。

用語説明：
*   **Cloud DNS**: Google Cloudが提供するスケーラブルでマネージドな権威DNSサービスです。
*   **CNAME レコード (Canonical Name Record)**: ドメイン名が別のドメイン名の別名であることを示すDNSレコードです。例えば、`www.example.com` を `example.com` の別名として定義する場合に利用されます。
*   **CNAME チェイシング (CNAME Chasing)**: DNSリゾルバがCNAMEレコードを辿って、最終的なIPアドレス（AレコードやAAAAレコード）を見つけるプロセスを指します。
*   **Private Zone**: Google CloudのVPCネットワーク内部でのみ解決可能なDNSゾーンです。内部リソースの名前解決に利用されます。
*   **Response Policy**: VPCネットワーク内のDNSクエリに対して、特定のドメイン名に対するカスタム応答（例えば、特定のIPアドレスへの強制ルーティング）を定義するためのポリシーです。
*   **VPC Name Resolution Order**: VPCネットワーク内部でのDNSクエリが解決される際の、様々なソース（レスポンスポリシー、プライベートゾーン、フォワーディングゾーン、ピアリングゾーン、内部DNS、パブリックゾーン）の優先順位を定めたものです。
*   **NXDOMAIN**: DNSクエリの結果として、指定されたドメイン名が存在しないことを示すエラー応答です。
*   **TTL (Time-To-Live)**: DNSレコードがキャッシュされる時間を示す値です。

## Announcement
原文:
Starting January 5, 2027, Cloud DNS will disable full responses to DNS queries of type `ANY` (`QTYPE=ANY`) in public authoritative zones. Instead, a single resource record will return for `ANY` queries, chosen from the existing resource record sets that match the query.

[public authoritative zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview)
Standard traffic from web browsers, applications, and API traffic query specific record types directly and are therefore unaffected with no action required.

However, certain legacy scripts, automated health checkers, debugging commands (for example, `dig example.com ANY`), or custom third-party monitoring systems that explicitly query `ANY` records will receive the first available record instead of a full zone inventory. You must complete the following configuration updates before January 5, 2027:

- **Identify legacy queries**: Review internal tools, deployment scripts, or third-party DNS monitoring configurations for commands or API calls that request the `ANY` record type. Cloud DNS logs in Cloud Logging can be helpful with this.
- **Transition to specific queries**: Update the tools to query the specific, individual record types they require (for example, querying for `A`, `AAAA`, `MX`, or `TXT` records separately).
- **Retrieve full zone records**: If you use `ANY` queries to retrieve all records in a zone, use the Cloud DNS REST API (`resourceRecordSets.list`), the gcloud CLI (`gcloud dns record-sets list`), or the Google Cloud Console instead.

Risks associated with not making these changes include the following:

- **False monitoring alarms**: Automated uptime or DNS monitoring tools checking `ANY` responses may misinterpret the new response as a system failure and trigger false alerts.
- **Broken automation pipelines**: Internal deployment or CI/CD scripts that rely on parsing a full zone dump with an `ANY` query will fail to retrieve the expected data payload and may crash.
- **Disrupted IT diagnostics**: Network administrators running manual legacy troubleshooting commands will no longer see a quick summary of all domain records, which could delay active network incident diagnostics.

説明：
2027年1月5日より、Cloud DNSのパブリック権威ゾーンにおける`ANY`タイプ(`QTYPE=ANY`)のDNSクエリに対する応答挙動が変更されます。これまではゾーン内の全レコードが返されていましたが、変更後はクエリに一致する単一のリソースレコードのみが返されるようになります。一般的なWebブラウザやアプリケーションからのトラフィックは特定のレコードタイプをクエリするため影響を受けませんが、レガシースクリプト、自動ヘルスチェッカー、デバッグコマンド、カスタム監視システムなど、明示的に`ANY`レコードをクエリするものは影響を受けます。

影響有無：
**影響あり。**
これも将来的な変更（2027年1月5日以降）ですが、現在`ANY`クエリをゾーン内の全レコード取得や診断目的で使用しているシステムがある場合、その動作が変更されるため影響を受けます。これにより、監視システムからの誤ったアラート、自動化パイプラインの停止、トラブルシューティングの困難化などの問題が発生する可能性があります。

対処方法：
2027年1月5日までに、以下の手順で対応してください。
1.  **`ANY`クエリの特定**: Cloud DNSログ（Cloud Loggingで確認可能）を活用し、`ANY`レコードタイプを要求する内部ツール、デプロイスクリプト、サードパーティDNS監視設定を特定します。
2.  **特定のクエリへの移行**: ツールやスクリプトを更新し、必要な個々のレコードタイプ（例: `A`, `AAAA`, `MX`, `TXT`など）を具体的にクエリするように変更します。
3.  **全ゾーンレコードの取得方法変更**: ゾーンの全レコードを取得する必要がある場合は、DNS REST API (`resourceRecordSets.list`)、`gcloud` CLI (`gcloud dns record-sets list`)、またはGoogle Cloudコンソールを使用するように変更します。

用語説明：
*   **`ANY` クエリ (`QTYPE=ANY`)**: DNSクエリにおいて、特定のレコードタイプを指定せず、利用可能な全てのレコードタイプを要求するクエリです。
*   **Public authoritative zones**: 公開されているDNSレコードを管理し、そのドメインに対する権威ある情報を提供するDNSゾーンです。
*   **Resource Record Set**: DNSゾーン内の、同じ名前とタイプを持つ全てのレコード（例：`example.com` の全てのAレコード）の集合を指します。
*   **Cloud Logging**: Google Cloudのフルマネージド型ロギングサービスで、Google Cloudリソースからのログを収集、保存、分析できます。
*   **REST API**: Webサービス間の通信で広く使われるアーキテクチャスタイルで、HTTPメソッド（GET, POSTなど）を使ってリソースを操作します。
*   **gcloud CLI**: Google Cloudリソースをコマンドラインから管理するための主要なツールです。
*   **Google Cloud Console**: Google Cloudリソースを管理するためのウェブベースのユーザーインターフェースです。

---

# Cloud SDK

## Breaking
原文:
Breaking

説明：
Cloud SDKに関するリリースノートのセクションですが、具体的な変更内容や詳細は提供されていません。「Breaking」というカテゴリは通常、既存のシステムやアプリケーションの動作に影響を与える可能性がある後方互換性のない変更を示します。

影響有無：
**影響不明。**
具体的な変更内容が記載されていないため、現時点では影響の有無を判断できません。しかし、「Breaking」というカテゴリから、もし利用中のCloud SDKバージョンが影響を受ける場合は、既存のスクリプトやアプリケーションに何らかの修正が必要になる可能性があります。

対処方法：
Cloud SDKの今後のリリースノートや公式ドキュメントで詳細が公開されるまで、定期的に情報を確認してください。利用中のCloud SDKバージョンに影響があるBreaking Changeが導入された場合は、SDKのアップデートと、それに関連するスクリプトやアプリケーションコードの修正が必要になる可能性があります。

用語説明：
*   **Cloud SDK**: Google Cloudリソースをコマンドラインから操作するためのツールセットです。これには`gcloud`コマンドラインツール、クライアントライブラリ、エミュレータなどが含まれます。
*   **Breaking Change (後方互換性のない変更)**: 新しいバージョンにアップグレードすると、既存のコードや設定が動作しなくなる可能性のある変更を指します。このような変更は、通常、アップグレード時に手動での修正作業を必要とします。
# Title: October 26, 2026 
Link: https://docs.cloud.google.com/release-notes#October_26_2026<br>
はい、Google Cloudのリリースノートを元に、構築済みのサービス（Google Cloud Composer2, Compoer version 2.7.1、Airflow version 2.7.3）への影響を調査し、簡潔に回答いたします。

---

# Apigee X
## Security
原文:
On October 24, 2026, we published a security bulletin for Apigee.
Two vulnerabilities in PHP core
(CVE-2026-109618
and
CVE-2026-109619,
"PHP2Shell") allow an unauthenticated attacker to execute code remotely on a
server running a vulnerable PHP version. The impact is limited to Drupal-based
Apigee developer portals, which customers deploy and operate. Apigee, Apigee
Hybrid, and the Apigee integrated portal don't use PHP and aren't affected.
Security bulletin published: GCP-2026-072

説明：
Apigeeに関して、2つのPHPコアの脆弱性（CVE-2026-109618、CVE-2026-109619、通称 "PHP2Shell"）に関するセキュリティ速報（GCP-2026-072）が公開されました。これらの脆弱性により、認証されていない攻撃者が脆弱なPHPバージョンを実行しているサーバー上でリモートコードを実行する可能性があります。この影響は、お客様がデプロイおよび運用しているDrupalベースのApigee Developer Portalに限定されます。Apigee本体、Apigee Hybrid、およびApigee統合ポータルはPHPを使用していないため、影響を受けません。

影響有無：
影響なし。
理由：
現在利用中のサービスはGoogle Cloud Composerであり、Apigee Xのサービスとは直接関連がありません。また、Apigee Xをご利用の場合でも、Apigee本体、Apigee Hybrid、またはApigee統合ポータルはPHPを使用していないため、この脆弱性の影響を受けません。影響を受けるのは、お客様が個別にデプロイ・運用しているDrupalベースのApigee Developer Portalのみです。

対処方法：
なし。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures)**: 公開されている情報セキュリティの脆弱性や露出に識別子を付与し、リスト化したものです。セキュリティ上の問題点を世界共通の識別子で管理し、情報の共有と対処を効率化します。
*   **リモートコード実行 (Remote Code Execution, RCE)**: 攻撃者が、ネットワークを介して遠隔地のコンピュータ上で、任意のプログラムコードを実行できてしまう脆弱性のことです。

---

# Compute Engine
## Security
原文:
A vulnerability (CVE-2026-85299) about incorrect authorization in
Compute Engine was discovered and has been addressed. For more information,
see the
GCP-2026-073 security bulletin.

説明：
Compute Engineにおいて、認証不備（Incorrect Authorization）に関する脆弱性（CVE-2026-85299）が発見され、Googleによって既に対処されました。詳細については、セキュリティ速報GCP-2026-073を参照してください。

影響有無：
影響なし。
理由：
この脆弱性はGoogle Cloudによって既に対処済みであり、お客様側での追加の対応は不要です。

対処方法：
なし。

用語説明：
*   **認証不備 (Incorrect Authorization)**: システムがユーザーやプロセスが特定のリソースにアクセスしたり、特定の操作を実行する権限を持っているかを検証する際に誤りがある状態を指します。これにより、権限のないユーザーが本来アクセスできない情報にアクセスしたり、操作を実行したりする可能性が生じます。

---

# Google Kubernetes Engine
## Change / Security (統合した説明)
原文:
GKE cluster versions have been updated.
New versions available for upgrades and new clusters.
The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see GKE versioning and
support and About GKE
cluster upgrades.
(中略 - 各チャネルでのバージョン更新、非推奨化、自動アップグレードターゲットの記述)
This release includes new GKE versions that use updated
Container-Optimized OS images. These updated images are cumulative,
incorporating security fixes from all Container-Optimized OS
versions released since the previous GKE release.

説明：
Google Kubernetes Engine (GKE) のクラスタバージョンが更新されました。
このリリースでは、各リリースチャネル（No channel (deprecated), Stable, Regular, Rapid, Extended）において、新しいGKEバージョンが利用可能となり、クラスタ作成のデフォルトバージョンも更新されました。また、一部の古いバージョンは非推奨化され、90日以内またはサポート終了時に削除される予定です。GKEクラスタのコントロールプレーンおよびノードの自動アップグレードターゲットバージョンも更新されました。
さらに、新しいGKEバージョンには更新されたContainer-Optimized OS (COS) イメージが含まれており、これには以前のGKEリリース以降にリリースされたすべてのCOSバージョンからの累積的なセキュリティ修正が含まれています。各COSイメージのリリースノートで、具体的な脆弱性修正内容を確認できます。

影響有無：
影響なし。
理由：
現在ご利用中のGoogle Cloud Composer 2.7.1 は、GKEバージョン 1.25.*、1.26.*、1.27.*、1.28.* をサポートしています。今回のリリースノートでアナウンスされたGKEのバージョンは1.31.*以降であり、現在ご利用のComposer環境に直接的なバージョンアップが適用されるものではありません。
ただし、GKEのセキュリティ更新は基盤となるContainer-Optimized OSイメージのセキュリティ向上に寄与するものであり、Composerが利用するGKEバージョンにおいても、将来的に同様のセキュリティアップデートが適用されることで、基盤のセキュリティ強化の恩恵を受けると予想されます。
非推奨化されるGKEバージョンについても、現時点ではご利用のComposer環境のGKEバージョンに直接該当するものはありませんが、将来的にComposerのバージョンアップを検討する際には、対象のGKEバージョンが非推奨化されないか確認が必要です。

対処方法：
なし。
現在のGoogle Cloud Composer環境においては、直接的な対処は不要です。
将来的にComposerまたはGKEのバージョンアップを計画する際には、本リリースノートで更新されたGKEバージョン情報や、非推奨化されるバージョンの影響範囲を事前に確認することを推奨します。

用語説明：
*   **GKE リリースチャネル**: GKEは、クラスタの安定性、機能の新規性、自動アップグレードの頻度に応じて複数のリリースチャネルを提供しています。ユーザーは自身のニーズに合わせて、安定性重視のStable、新機能も取り込むRegular、最新機能を試せるRapid、長期サポートのExtendedなどを選択できます。
*   **Container-Optimized OS (COS)**: Googleによって最適化された、コンテナワークロードの実行に特化したオペレーティングシステムです。GKEクラスタのノードの基盤として使用され、セキュリティと効率性を高めるように設計されています。
*   **自動アップグレードターゲット**: GKEクラスタのコントロールプレーンやノードが、自動的にアップグレードされる際の目標となるバージョンを指します。GKEは、メンテナンスウィンドウやチャネルポリシーに基づいて、指定されたターゲットバージョンへの自動アップグレードを実行します。
*   **非推奨 (Deprecated)**: 特定の機能やバージョンが、将来的にサポートされなくなるか、または完全に削除される予定であることを示す状態です。通常、代替の機能やバージョンが提供されます。
# Title: October 24, 2026 
Link: https://docs.cloud.google.com/release-notes#October_24_2026<br>
Google Cloudのインフラエンジニアとして、ご担当のCloud Runサービスへの影響について調査しました。

---

# Cloud Run
## Announcement
原文:
The following runtime languages contain important security updates:

- Go 1.24 and later: `1.24.13`, `1.25.14`, `1.26.10`, `1.27.3`
- Node.js 22 and later: `22.23.4`, `24.22.1`, `26.12.1`
- Java 17 and later: `17.0.20_101`, `21.0.12_101.0.LTS`, `25.0.5_8.0.LTS`
- PHP 8.2 and later: `8.2.35`, `8.3.36`, `8.4.27`, `8.5.12`
- Python 3.10 and later: `3.10.22`, `3.11.17`, `3.12.15`, `3.13.15`, `3.14.6`
- Ruby 3.3 and later: `3.3.12`, `3.4.11`, `4.0.7`
- .NET 6 and later: `6.0.428`, `8.0.415`, `10.0.100`

The following stacks and their underlying operating system packages have also been updated:

- `google-22`, `google-22-full`
- `google-24`, `google-24-full`

Take immediate protective action by rebuilding and redeploying your resources with updated dependencies.

See Security bulletins for Google Cloud for more information.

説明:
Cloud Runがサポートする主要なランタイム言語（Go, Node.js, Java, PHP, Python, Ruby, .NET）について、重要なセキュリティアップデートが適用されたことが発表されました。これにより、これらのランタイムの新しいバージョンが利用可能になっています。
また、Cloud Runの基盤となるオペレーティングシステムパッケージを含むスタックイメージ (`google-22`, `google-22-full`, `google-24`, `google-24-full`) も更新されました。
Google Cloudは、これらのセキュリティアップデートを反映させるため、Cloud Run上にデプロイされているリソース（サービス）を最新の依存関係で再ビルドし、再デプロイすることを強く推奨しています。これにより、潜在的なセキュリティ脆弱性からサービスを保護できます。

影響有無:
**影響あり。**
現在稼働しているCloud Runサービスが、上記の対象ランタイム言語のいずれかを使用している場合、セキュリティ脆弱性のリスクを低減するために対応が必要です。既存のデプロイが直ちに停止することはありませんが、セキュリティリスクを抱えた状態となります。このアップデートは、基盤となるランタイムやOSパッケージのセキュリティ強化を目的としており、アプリケーションコードの機能的な変更は伴いませんが、セキュリティ体制を維持するためには必須の対応です。

対処方法:
1.  **対象サービスの特定:** ご利用中のCloud Runサービスが、リリースノートに記載されているGo, Node.js, Java, PHP, Python, Ruby, .NETのいずれかのランタイムを使用しているか確認してください。
2.  **再ビルドと再デプロイ:** 該当するCloud Runサービスについて、アプリケーションを最新の依存関係が取り込まれる形で再ビルドし、Cloud Runに再デプロイしてください。
    *   `cloud build` などのCI/CDパイプラインを利用している場合は、パイプラインを再実行することで、最新のベースイメージやランタイムが使用されます。
    *   Dockerfileで独自のベースイメージを指定している場合は、ベースイメージが最新のセキュリティパッチを含んでいることを確認してください。
3.  **セキュリティ速報の確認:** 今後もGoogle Cloudのセキュリティ速報（[Security bulletins for Google Cloud](https://docs.cloud.com/support/bulletins)）を定期的に確認し、Cloud Runだけでなく、他のGoogle Cloudサービスに関する追加情報や詳細な脆弱性情報にも注意を払ってください。

用語説明:
*   **ランタイム (Runtime):** プログラムを実行するために必要なソフトウェア環境のことです。これには、プログラミング言語の実行エンジン、標準ライブラリ、およびその他の必要なコンポーネントが含まれます。Cloud Runでは、アプリケーションが動作する特定の言語バージョン環境を指します。
*   **スタックイメージ (Stack Image):** Cloud Runが提供する、特定のランタイムと基盤となるオペレーティングシステム（OS）パッケージが事前に構成された環境イメージです。ユーザーがアプリケーションコードをデプロイする際に、これらのビルド済みイメージを利用することで、環境構築の手間を省けます。
*   **セキュリティアップデート (Security Update):** ソフトウェア製品に含まれるセキュリティ上の脆弱性（弱点や欠陥）を修正するために提供される更新プログラムです。これを適用することで、不正アクセス、データ漏洩、サービス妨害などの潜在的なセキュリティリスクを軽減できます。
*   **再ビルド (Rebuilding):** ソースコードと依存関係（ライブラリなど）から、実行可能なアプリケーションイメージを再度作成するプロセスです。このプロセスにより、最新のセキュリティパッチや機能改善が取り込まれます。
*   **再デプロイ (Redeploying):** 既に稼働しているサービスに対して、新しくビルドされたアプリケーションイメージを配置し、サービスを更新する作業です。これにより、最新の機能やセキュリティ修正が反映されたバージョンでサービスが稼働し始めます。