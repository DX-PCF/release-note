
# Title: August 13, 2026 
Link: https://docs.cloud.google.com/release-notes#August_13_2026<br>
Google Cloud インフラエンジニアとして、Apigee X のリリースノートに関する調査結果を以下にご報告いたします。

---

# Apigee X

## Announcement

**原文**:
 On August 13th, 2026, we began maintenance updates of Apigee instances configured for maintenance windows.
 If you set a preferred window for maintenance for your instance, and your instance version is
below **1-18-0-apigee-2**, your instance will be updated to **1-18-0-apigee-2** within the
next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.
 Note: Instances that meet either of the following two criteria will not be updated:
 - Your instance has a DNS misconfiguration, as described in Known Issue 445936920.
 - Your instance uses an Apigee Java Library that has been removed, as described in Apigee release notes dated October 16, 2025.
 For more information on participating in scheduled maintenance windows, see Maintenance overview and Manage Apigee instance maintenance windows.

**説明**:
2026年8月13日から、メンテナンスウィンドウを設定しているApigeeインスタンスのメンテナンスアップデートが開始されました。
お使いのApigeeインスタンスがメンテナンスウィンドウを設定しており、かつ現在のバージョンが「1-18-0-apigee-2」未満である場合、今後7〜21日以内に「1-18-0-apigee-2」へ自動的にアップデートされます。アップグレード予定日を含む通知は、今後2営業日以内に送信される予定です。
ただし、以下のいずれかの条件に該当するインスタンスはアップデートされません。
1.  Known Issue 445936920 に記載されているDNS設定の誤りがあるインスタンス。
2.  2025年10月16日のApigeeリリースノートで削除されたと記載されているApigee Javaライブラリを使用しているインスタンス。
詳細は、Apigeeの公式ドキュメント「Maintenance overview」および「Manage Apigee instance maintenance windows」を参照してください。

**影響有無**:
*   **影響あり**: メンテナンスウィンドウを設定しており、かつApigee Xインスタンスのバージョンが「1-18-0-apigee-2」未満の場合、指定されたバージョンに自動アップグレードされます。これにより、サービスの安定性やセキュリティが向上する一方で、アップグレード期間中の挙動変化や予期せぬ問題発生の可能性に備える必要があります。
*   **影響なし**: メンテナンスウィンドウを設定していないインスタンス、または既に「1-18-0-apigee-2」以上のバージョンであるインスタンスは、このアナウンスによる直接的なアップグレードの影響を受けません。また、DNS設定の誤りや削除されたJavaライブラリの使用によりアップデートがスキップされる場合も、直接的なアップデートの影響は受けません（ただし、これらの問題自体は別途対処が必要です）。

**対処方法**:
1.  **インスタンスバージョンの確認**: お使いのApigee Xインスタンスの現在のバージョンを確認します。
2.  **通知の確認と社内共有**: 今後2営業日以内に送信されるアップグレード予定日の通知を確認し、社内関係者への情報共有、および必要に応じてアップグレード期間中の監視体制強化を検討します。
3.  **DNS設定の確認**: Known Issue 445936920 に記載されているDNS設定の誤りがないか確認し、もし該当する場合は速やかに修正します。
4.  **Javaライブラリ使用状況の確認**: 2025年10月16日のリリースノートで削除されたApigee Javaライブラリを使用していないか確認し、該当する場合は代替手段への移行を検討します。
5.  **サービスへの影響評価**: アップグレードが実施されることを踏まえ、APIの動作確認やログの監視を強化し、異常がないか継続的に確認します。

**用語説明**:
*   **メンテナンスウィンドウ (Maintenance Window)**: クラウドサービスプロバイダがシステム保守やアップグレードを行うために、ユーザーが事前に設定できる時間枠。この時間帯にメンテナンスが実施されることで、ユーザーのサービスへの影響を最小限に抑えるよう配慮されます。
*   **Apigee X**: Google Cloudが提供するフルマネージドのAPI管理プラットフォーム。APIの設計、デプロイ、セキュリティ、監視、分析などを提供します。
*   **インスタンス (Instance)**: Apigee Xサービスが動作している論理的な実行環境の単位を指します。

---

## Announcement

**原文**:
 On August 13th, 2026, we released an updated version of Apigee (1-18-0-apigee-3).
 > **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

**説明**:
2026年8月13日に、Apigeeの更新バージョン「1-18-0-apigee-3」がリリースされました。このリリースのロールアウトは本日開始され、すべてのGoogle Cloudゾーンで完了するまでに4営業日以上かかる場合があります。ロールアウトが完了するまで、お使いのインスタンスでは新機能や修正が利用できない可能性があります。

**影響有無**:
*   **影響あり**: リリースされた新バージョンには、後述するバグ修正やセキュリティパッチが含まれており、これらの恩恵を受けることができます。しかし、ロールアウトは段階的に行われるため、すべてのインスタンスにすぐに適用されるわけではありません。機能や修正が利用可能になるまでの間、一時的に環境間でバージョン差が生じる可能性があります。
*   **影響なし**: 即座に既存のワークロードに悪影響を及ぼす可能性は低いですが、新しい修正や機能がすぐに適用されない可能性があるという「潜在的な」影響はあります。

**対処方法**:
1.  **機能や修正の利用計画**: リリースノートに記載されている修正や新機能を活用する予定がある場合、インスタンスへのロールアウトが完了するまで待つ必要があります。特定の機能に依存する計画がある場合は、ロールアウト状況を適宜確認することが推奨されます。
2.  **継続的な監視**: リリースされた新しいバージョンがインスタンスに適用された後、既存のAPIプロキシやアプリケーションの動作に予期せぬ影響がないか、継続的に監視を行います。

**用語説明**:
*   **ロールアウト (Rollout)**: 新しいソフトウェアバージョンや機能が段階的に導入され、すべてのシステムやユーザーに展開されるプロセスを指します。
*   **Google Cloud zones**: Google Cloudリソースが配置される地理的な場所の単位。特定のリージョン内の独立した障害ドメインを表します。

---

## Fixed

**原文**:
| Bug ID | Description |
| --- | --- |
| **532147587** | To fix forward proxy support. |
| **537657987** | Fixed a bug where watcher failed to reconcile all routes if an environment was not found in the control plane. |
| **543022076** | Google Cloud BOM upgrade (protobuf 4.x, gRPC 1.81, Guava 33.5). One user-visible change: a malformed inbound gRPC request frame is now reported to the client as grpc-status INTERNAL(13) and recorded in analytics as x-apigee.grpc.status=13, where it was previously an Apigee ServiceUnavailable fault seen as UNAVAILABLE(14) with no x-apigee.grpc.status recorded. Otherwise no user facing impact, but any prod issue related to gcp, protobuf or gRPC may relate to this. |
| **542242046** | Fixed LLMTokenQuota metering the request against an arbitrary quota bucket when the API Product declared multiple models and the request carried no model. |
| **531731614** | Apigee analytics fields ai_llm_response_token_count, ai_llm_prompt_token_count, ai_llm_model_name, and ai_llm_model_provider are available in the Custom Report when LLMTokenQuota and PromptTokenLimit policies are used in Apigee proxies. |
| **492044413** | LLMTokenQuota resolves the model from the API Product LLM Operation when LLMModelSource is omitted and the request body has no model field. |
| **67169710** | Adds an opt-in <DynamicClientIdSupported> boolean XML element to the OAuthV2 policy. When true, AbstractOAuthStepExecution.extractClientDetails() preserves any non-empty ClientID/ClientSecret already present on the OAuthClientContext. |
| **531731614** | Apigee auto identifies the providers and publishes them to analytics. |
| **537396574** | Added feature to rotate the apigee-ca certificate. |
| **540861752** | Aligned the ApigeeDeployment conversion hub with its v1alpha3 storage version. Internal change; no effect on existing ApigeeDeployment resources. |
| **540861752** | Aligned the ApigeeDeployment custom resource's conversion hub with its v1alpha3 storage version. This internal change does not affect existing ApigeeDeployment resources. |
| **N/A** | Updates to infrastructure and libraries.

**説明**:
複数のバグ修正と機能改善が実施されました。主な変更点は以下の通りです。
*   **フォワードプロキシのサポート改善**: フォワードプロキシを利用している環境の安定性が向上します。
*   **ルーティングの整合性改善**: コントロールプレーンで環境が見つからない場合に、watcherがすべてのルートを調整できないバグが修正されました。
*   **Google Cloud BOMアップグレード**: `protobuf 4.x`, `gRPC 1.81`, `Guava 33.5` などの基盤ライブラリがアップグレードされました。これにより、不正なgRPCリクエストフレームに対するクライアントへのエラーレポートが `grpc-status INTERNAL(13)` に変更され、アナリティクスに `x-apigee.grpc.status=13` が記録されるようになります（以前は `UNAVAILABLE(14)`）。
*   **LLMTokenQuotaの改善**: 複数のモデルが宣言されているAPI Productに対し、リクエストでモデルが指定されていない場合に、LLMTokenQuotaが不適切なクォータバケットに対してメーターリングを行うバグが修正されました。また、`LLMModelSource`が省略され、リクエストボディにモデルフィールドがない場合でも、LLMTokenQuotaがAPI ProductのLLM操作からモデルを解決するようになりました。
*   **LLM関連アナリティクスの拡張**: LLMTokenQuotaおよびPromptTokenLimitポリシーがApigeeプロキシで使用されている場合、`ai_llm_response_token_count`、`ai_llm_prompt_token_count`、`ai_llm_model_name`、`ai_llm_model_provider`などのAI関連アナリティクスフィールドがカスタムレポートで利用可能になりました。Apigeeがプロバイダを自動識別し、アナリティクスに公開する機能も改善されました。
*   **OAuthV2ポリシーの機能追加**: `DynamicClientIdSupported`というboolean型のXML要素がOAuthV2ポリシーに追加されました。これを`true`に設定すると、`AbstractOAuthStepExecution.extractClientDetails()`が`OAuthClientContext`に既に存在する非空の`ClientID`/`ClientSecret`を保持するようになります。
*   **Apigee-CA証明書のローテーション機能追加**: Apigee-CA証明書をローテーションする機能が追加されました。
*   **内部的なリソース調整**: `ApigeeDeployment`変換ハブが`v1alpha3`ストレージバージョンに整合されました。これは内部変更であり、既存の`ApigeeDeployment`リソースには影響しません。
*   **インフラストラクチャおよびライブラリの更新**: 一般的なインフラストラクチャとライブラリの更新が含まれます。

**影響有無**:
*   **影響あり（改善/機能追加）**:
    *   **gRPCトラフィック利用者**: 不正なgRPCリクエストフレームに対するエラーレポートの形式が変わるため、アプリケーションや監視システムでこの変更を考慮する必要があります。
    *   **LLMTokenQuota利用者**: ポリシーの動作がより正確になり、API Productのモデル定義からの解決が改善されます。
    *   **LLM関連アナリティクス利用者**: より詳細なAI関連の分析データがカスタムレポートで利用可能になり、分析能力が向上します。
    *   **OAuthV2ポリシー利用者**: `DynamicClientIdSupported`オプションの追加により、OAuthフローの柔軟性が向上する可能性があります。
    *   **セキュリティ強化**: `apigee-ca`証明書のローテーション機能が追加され、セキュリティ体制が強化されます。
*   **影響なし**: `ApigeeDeployment`リソースに関する内部的な変更は、既存のリソースに直接的な影響を与えません。一般的なインフラストラクチャおよびライブラリの更新も、通常、ユーザーに直接的な影響はありませんが、パフォーマンス向上や安定性向上が期待されます。

**対処方法**:
1.  **gRPCエラーハンドリングの確認**: `gRPC-status INTERNAL(13)` の新しいエラーコードに対応できるよう、アプリケーションや監視システムのエラーハンドリングロジック、およびログ解析設定を確認し、必要に応じて更新します。
2.  **LLMTokenQuotaの利用状況確認**: LLMTokenQuotaポリシーを利用している場合は、修正によって期待通りの挙動を示すか確認し、必要に応じてポリシー設定を見直します。
3.  **アナリティクスレポートの活用**: LLM関連のアナリティクスが利用可能になったため、カスタムレポートを作成してAI関連のAPI利用状況を詳細に分析することを検討します。
4.  **OAuthV2ポリシーの利用検討**: `DynamicClientIdSupported`オプションの追加により、OAuthV2ポリシーの柔軟性が向上します。既存のOAuthフローで`ClientID`/`ClientSecret`の保持が必要な場合は、この機能の導入を検討します。
5.  **証明書ローテーションの検討**: `apigee-ca`証明書のローテーション機能が追加されたため、組織のセキュリティポリシーに基づき、定期的な証明書ローテーションプロセスを検討・実施します。
6.  **全般的な動作確認**: アップデート適用後、既存のAPIプロキシの機能テスト、パフォーマンス監視、ログ監視などを実施し、予期せぬ問題が発生していないことを確認します。

**用語説明**:
*   **フォワードプロキシ (Forward Proxy)**: クライアントからのリクエストを代理してWebサーバに送信するプロキシサーバ。
*   **コントロールプレーン (Control Plane)**: クラウドインフラストラクチャにおいて、リソースの管理、オーケストレーション、設定、監視などを行う部分。データプレーン（実際のデータトラフィックが流れる部分）と対比されます。
*   **Google Cloud BOM (Bill Of Materials)**: Google Cloudのサービスが使用する依存ライブラリのバージョン集合。一貫性のある動作と互
# Title: August 12, 2026 
Link: https://docs.cloud.google.com/release-notes#August_12_2026<br>
Google Cloudインフラエンジニアとして、ご提示いただいたリリースノートについて、構築済みのサービス（Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)）への影響有無を調査し、簡潔に回答いたします。

---

# BigQuery
## Announcement
原文: Table Explorer behavior has moved to the **Reference** panel. Table Explorer has been deprecated. For more information, see "Use the Reference panel" in Run a query.
[Run a query](https://docs.cloud.google.com/bigquery/docs/running-queries#use-reference-panel)

説明：BigQuery コンソールのクエリ実行画面において、「Table Explorer」機能が非推奨となり、「Reference」パネルに機能が統合されました。

影響有無：**影響なし**
この変更はBigQueryコンソール（Web UI）の操作性に関するものであり、既存のBigQueryデータやクエリの実行、APIを通じたプログラムからの操作に直接的な影響はありません。Google Cloud ComposerからBigQueryを操作する際は、主にSQLクエリの実行やAPIコールを使用するため、今回のUI変更はComposerの動作には影響しません。

対処方法：BigQueryコンソールで「Table Explorer」を利用されていた場合は、今後は「Reference」パネルを使用するように操作方法を切り替えてください。

用語説明：
*   **Table Explorer:** BigQueryコンソールのクエリエディタ画面のサイドパネルに表示されていた機能で、テーブルのスキーマやプレビューなどを確認できました。
*   **Reference panel:** BigQueryコンソールのクエリエディタ画面で、プロジェクト、データセット、テーブル、ストアドプロシージャ、ビューなどを参照できるパネルです。

---

# Google Kubernetes Engine
## Change
原文: GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.
[GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)

説明：GKEのクラスターバージョンが更新されました。新しいクラスターの作成や、既存クラスターのコントロールプレーンおよびノードのアップグレードで利用可能なバージョンが増え、いくつかのバージョンが非推奨となりました。

### No channel (deprecated)
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.35.6-gke.1258000 is now the default version for cluster creation.
- The following versions are now available:
    - 1.33.13-gke.1414000
    - 1.34.10-gke.1079000
    - 1.35.5-gke.1163012
    - 1.35.5-gke.1241004
    - 1.35.7-gke.1027000
    - 1.36.3-gke.1244000
    - 1.36.3-gke.1253000
- The following node versions are now available:
    - 1.31.14-gke.2543000
    - 1.32.13-gke.2231000
    - 1.33.13-gke.1414000
    - 1.34.10-gke.1079000
    - 1.35.7-gke.1027000
    - 1.36.3-gke.1244000
    - 1.36.3-gke.1253000
- The following versions are no longer available:
    - 1.33.12-gke.1270000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
    - 1.34.9-gke.1131000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
    - 1.35.6-gke.1127000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
    - 1.36.2-gke.2281000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
[... (略) ...]

### 各チャンネルの変更 (Stable, Regular, Rapid, Extended)
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- The following versions are now available in the Stable channel: [...]
- The following versions are no longer available in the Stable channel: [...]
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. [...]
[... (各チャンネルで同様の内容が続く) ...]

説明：GKEの各リリースチャンネル（No channel, Stable, Regular, Rapid, Extended）において、利用可能な新しいバージョンが追加され、同時に一部の古いバージョンが非推奨（deprecated）となりました。非推奨となったバージョンは、90日以内、またはサポート終了の早い方で削除されます。また、各チャンネルでの自動アップグレードのターゲットバージョンも更新されています。

影響有無：**影響あり（要確認）**
Google Cloud Composer 2は基盤としてGKEクラスタを使用しているため、GKEバージョンの更新は関連性があります。
Composerはマネージドサービスであり、通常、基盤となるGKEのバージョン管理（アップグレード含む）はGoogle Cloud側で自動的に行われ、Composerサービスの互換性が維持されます。しかし、以下を確認する必要があります。
1.  **現在利用中のGKEバージョン:** 現在のComposer環境が稼働しているGKEクラスタのバージョンを確認してください。特に、リリースノートで「deprecated」とされているバージョン（例: `1.33.12-gke.1270000`, `1.34.9-gke.1131000`, `1.35.6-gke.1127000`, `1.36.2-gke.2281000`）に該当しないか確認が必要です。該当する場合、これらのバージョンは90日以内にサポート対象外となるため、Composerが自動アップグレードの対象となる可能性が高いです。
2.  **ComposerのGKEバージョンサポート:** Composer 2.7.1がサポートするGKEのバージョン範囲を確認してください。通常、Composerのドキュメントに記載されています。

対処方法：
1.  **GKEバージョンの確認:** Google Cloud コンソールのComposerまたはGKEのセクションから、現在お使いのComposer環境のGKEバージョンを確認してください。
2.  **非推奨バージョンへの対応:** もし現在のGKEバージョンがリリースノートに記載されている非推奨バージョンに該当する場合でも、Composerはマネージドサービスであるため、通常はGoogle Cloudが自動的にサポート対象バージョンへのアップグレードを管理します。ユーザー側で緊急にGKEクラスターの手動アップグレードを行う必要は稀ですが、念のためComposerの公式ドキュメントでComposer 2.7.1のGKEバージョンに関する方針を確認してください。
3.  **互換性テスト:** GKEの自動アップグレードが有効な場合、新しいGKEバージョンへのアップグレードが順次適用されます。本番環境への影響を最小限に抑えるため、可能な限りステージング環境などでComposerのワークフローが新しいGKEバージョンで正常に動作するかどうかを事前にテストすることを推奨します。

用語説明：
*   **GKE (Google Kubernetes Engine):** Google Cloudが提供するマネージドKubernetesサービスで、コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **コントロールプレーン (Control Plane):** Kubernetesクラスタの管理層であり、APIサーバ、スケジューラ、コントローラマネージャなどのコンポーネントを含みます。
*   **ノード (Node):** Kubernetesクラスタ内でコンテナ化されたワークロード（ポッド）を実行するワーカーマシンです。
*   **リリースチャンネル (Release Channel):** GKEクラスターのバージョンアップグレードのペースと安定性を管理するための設定です。Rapid、Regular、Stable、Extendedなどがあり、それぞれ新機能の導入速度やサポート期間が異なります。
*   **Deprecated (非推奨):** 将来的にサポートが終了し、削除される予定の機能やバージョンを指します。

## Security
原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release.
To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the **Security** release notes for that image. The following table includes links to the release notes for each updated Container-Optimized OS image:
| GKE version | Container-Optimized OS version | Details |
|---|---|---|
| 1.31.14-gke.2543000 | cos-117-18613-675-28 | cos-117-18613-675-28 release notes |
| 1.32.13-gke.2231000 | cos-117-18613-675-28 | cos-117-18613-675-28 release notes |
| 1.33.13-gke.1414000 | cos-121-18867-528-21 | cos-121-18867-528-21 release notes |
| 1.34.10-gke.1079000 | cos-125-19216-532-42 | cos-125-19216-532-42 release notes |
| 1.35.7-gke.1027000 | cos-125-19216-532-25 | cos-125-19216-532-25 release notes |
| 1.36.3-gke.1244000 | cos-129-19506-299-60 | cos-129-19506-299-60 release notes |

説明：本リリースに含まれる新しいGKEバージョンでは、セキュリティ修正が適用された最新のContainer-Optimized OS (COS) イメージが使用されています。これにより、以前のGKEリリース以降に公開されたすべてのCOSセキュリティ修正が累積的に適用されます。各COSイメージで解決された具体的な脆弱性は、対応するCOSリリースノートで確認できます。

影響有無：**ポジティブな影響あり**
GKEノードの基盤となるOSイメージにセキュリティ修正が適用されるため、Google Cloud Composerが稼働するGKE環境のセキュリティが向上します。これは既存のセキュリティ体制を強化するものであり、サービス運用に負の影響を与えるものではありません。

対処方法：
GKEクラスターの自動アップグレードが有効な場合、特別な対処は不要です。GKEが自動的にノードイメージを更新し、セキュリティが向上します。手動でアップグレードを管理している場合は、計画的にGKEバージョンアップグレードを実施し、最新のCOSイメージが適用されるようにしてください。

用語説明：
*   **Container-Optimized OS (COS):** Googleがコンテナワークロード向けに最適化して提供するLinuxベースのOSイメージです。セキュリティ、信頼性、性能を重視して設計されています。

---

# Identity and Access Management
## Change
原文: The workflow for creating workforce identity pool providers in the Google Cloud console changed. After submitting the initial provider configuration, the console directs you to a centralized page to configure provider attributes, including attribute mappings, attribute conditions, and extra attributes.
For more information, see Manage workforce identity pools and providers.
[Manage workforce identity pools and providers](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers)

説明：Google Cloudコンソールにおける「ワークフォースアイデンティティプールプロバイダ」の作成ワークフローが変更されました。初期プロバイダ設定を送信した後、属性マッピング、属性条件、追加属性などのプロバイダ属性を設定するための集中管理ページに誘導されるようになります。

影響有無：**影響なし**
この変更はGoogle Cloudコンソール（Web UI）におけるワークフォースアイデンティティプールプロバイダの**作成時**の操作フローに関するものです。既存のワークフォースアイデンティティプールやそのプロバイダの設定、およびAPIやTerraformなどを用いたプログラムによるIAM操作には直接的な影響はありません。Google Cloud Composerの運用に直接関連する変更ではありません。

対処方法：今後、Google Cloudコンソールでワークフォースアイデンティティプールプロバイダを新規に作成する際は、新しいワークフローに従って操作してください。

用語説明：
*   **Identity and Access Management (IAM):** Google Cloudリソースへのアクセス権限を管理するサービスです。
*   **ワークフォースアイデンティティプール (Workforce Identity Pool):** 従業員、パートナー、顧客などの外部ユーザー（"workforce"）が、自身の既存のIDプロバイダ（例: Okta, Azure ADなど）を使ってGoogle Cloudリソースにアクセスできるようにするための仕組みです。これにより、外部IdPとのフェデレーションによる認証・認可が可能になります。
*   **プロバイダ (Provider):** ワークフォースアイデンティティプールにおいて、外部のIDプロバイダ（IdP）との具体的な連携方法（認証プロトコル、属性マッピングなど）を定義する設定です。
# Title: August 11, 2026 
Link: https://docs.cloud.google.com/release-notes#August_11_2026<br>
Google Cloudのリリースノートに関する調査結果を以下にまとめます。

---

# Cloud SDK

## Breaking
原文:
(空行)

説明：
Cloud SDKのリリースノートにおいて、「Breaking」カテゴリに分類される変更がアナウンスされていますが、具体的な変更内容を示す原文が提供されていません。

影響有無：
原文が提供されていないため、具体的な変更内容を把握できず、お客様の既存の構成やサービスへの影響有無を判断できません。一般的に「Breaking」カテゴリの変更は、後方互換性のない変更を意味するため、何らかの対処が必要となる可能性が高いです。

対処方法：
Cloud SDKの公式リリースノートを参照し、「Breaking」カテゴリの該当箇所でどのような変更があったのかを確認してください。変更内容に応じて、既存のスクリプトやツール、CI/CDパイプラインなどでCloud SDKを使用している部分に修正が必要となる可能性があります。

用語説明：
*   **Cloud SDK**: Google Cloud Platformのサービスをコマンドラインから操作するためのツールセットです。gcloudコマンドラインツール、gsutil、bqなどが含まれます。
*   **Breaking Change**: 既存のシステムやアプリケーションの動作に影響を与える、後方互換性のない変更を指します。通常、APIの仕様変更、機能の削除、デフォルト値の変更などが該当します。

---

# Compute Engine

## Security
原文:
A vulnerability (CVE-2026-6726) in the Trusted Computing Group's TPM 2.0 reference implementation code was discovered and is being addressed.
For more information, see the
GCP-2026-054 security bulletin.

[GCP-2026-054 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-054)

説明：
Trusted Computing Group (TCG) の TPM 2.0 リファレンス実装コードにおいて、新たな脆弱性 (CVE-2026-6726) が発見されたことがアナウンスされています。この脆弱性に対しては現在、Google Cloudによって対応が進められています。詳細情報については、提供されているGCP-2026-054セキュリティ速報を参照するように促しています。

影響有無：
**影響あり**
Compute Engineは、仮想マシンインスタンスの基盤としてTPM 2.0互換の仮想TPM (vTPM) やセキュアブート機能を提供しています。お客様のCompute Engineインスタンスでこれらのセキュリティ機能（特にvTPM）を使用している場合、この脆弱性の影響を受ける可能性があります。Google Cloudは通常、基盤となるインフラストラクチャレベルで脆弱性への対応を行いますが、お客様が運用するVM内のOSやアプリケーションレベルでの確認、または追加の対応が必要になる場合があります。

対処方法：
1.  **GCP-2026-054セキュリティ速報の確認:** 提供されているリンク ([GCP-2026-054 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-054)) を確認し、脆弱性の詳細、影響範囲、Google Cloud側の対応状況、およびお客様側で推奨される具体的なアクション（例えば、OSのパッチ適用、設定の変更、ワークロード固有の緩和策など）を確認してください。
2.  **既存VMインスタンスの確認:** 運用中のCompute Engineインスタンスで、仮想TPM (vTPM) やセキュアブートが有効になっているかを確認してください。特にvTPMは、Windows ServerのCredential Guardなど特定のセキュリティ機能で利用されることがあります。
3.  **Google Cloudの対応状況の注視:** Google Cloudが基盤でパッチ適用や緩和策を展開する可能性があります。今後のアナウンスやセキュリティ速報の更新を定期的に確認してください。
4.  **Google Cloud Composerへの影響:** Google Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3) はCompute Engine上で動作するマネージドサービスです。基盤となるVMのセキュリティ脆弱性ですが、Composerの環境についてはGoogle Cloudがマネージドサービスとしてセキュリティパッチの適用や対策を行うことが期待されます。お客様側で直接Compute Engineインスタンスにアクセスしてパッチを適用する必要はありませんが、Google Cloudの公式アナウンスを注視し、必要に応じてComposerのバージョンアップや設定変更が推奨される可能性があります。

用語説明：
*   **TPM (Trusted Platform Module)**: コンピュータのセキュリティを強化するためのハードウェアベースの暗号プロセッサです。暗号鍵の生成、保存、保護、システムの整合性検証などに使用されます。仮想マシン環境では、仮想TPM (vTPM) として提供されます。
*   **CVE (Common Vulnerabilities and Exposures)**: 公開されている情報セキュリティの脆弱性に対して付与される、世界共通の識別子です。
*   **Trusted Computing Group (TCG)**: 信頼できるコンピューティング技術の標準を開発・推進する非営利団体です。TPMの仕様を策定しています。
*   **セキュリティ速報 (Security Bulletin)**: 特定のセキュリティ脆弱性や脅威に関する詳細情報、影響、推奨される対策を記載した公式アナウンスです。

---