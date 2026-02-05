
# Title: February 04, 2026 
Link: https://docs.cloud.google.com/release-notes#February_04_2026<br>
# BigQuery
## Change
原文: Data transfers from the YouTube Channel and YouTube Content Owner data sources now support reach reports. For more information, see YouTube Channel report transformation and YouTube Content Owner report transformation.

[YouTube Channel](https://docs.cloud.google.com/bigquery/docs/youtube-channel-transfer)
[YouTube Content Owner](https://docs.cloud.google.com/bigquery/docs/youtube-content-owner-transfer)
[YouTube Channel report transformation](https://docs.cloud.google.com/bigquery/docs/youtube-channel-transformation)
[YouTube Content Owner report transformation](https://docs.cloud.google.com/bigquery/docs/youtube-content-owner-transformation)

説明：
BigQuery Data Transfer Service を使用した YouTube Channel および YouTube Content Owner のデータソースからのデータ転送において、新たに「リーチレポート (reach reports)」がサポートされるようになりました。これにより、YouTubeアナリティクスデータとして、視聴者へのコンテンツ到達度に関する詳細なレポートをBigQueryに取り込むことが可能になります。

影響有無：
**影響なし（ただし、新規活用によるメリットあり）**

この変更は、BigQuery Data Transfer Service の機能追加であり、既存のデータ転送設定やスキーマに破壊的な変更をもたらすものではありません。したがって、現在 YouTube Channel/Content Owner のデータ転送を利用している場合でも、既存のデータパイプラインや分析クエリが自動的に変更されたり、動作に影響が出たりすることはありません。
しかし、新たにリーチレポートが利用可能になったことで、YouTubeデータの分析において、より詳細な「到達度」に関するインサイトを得ることが可能になります。これは、必要に応じて活用を検討できるプラスの機能追加です。

対処方法：
特段の対処は不要です。
もし、YouTubeコンテンツのリーチ（到達度）に関する詳細な分析が必要な場合は、BigQuery Data Transfer Service の既存の転送設定を見直すか、新規の転送設定を作成して、リーチレポートを含めることを検討してください。リーチレポートを含める場合は、関連するテーブルスキーマの変更が伴う可能性があるため、ダウンストリームのデータ処理やBIツールへの影響を確認し、必要に応じて改修を計画してください。

用語説明：
*   **BigQuery Data Transfer Service**: Google Cloud が提供するサービスで、外部データソース（SaaSアプリケーション、Googleの広告サービスなど）からBigQueryへデータを定期的に自動的に転送する機能を提供します。手動でのデータ取り込み作業を削減し、データウェアハウスを常に最新の状態に保つのに役立ちます。
*   **YouTube Channel data source**: BigQuery Data Transfer Service のデータソースの一つで、特定のYouTubeチャンネルに関連するアナリティクスデータ（視聴回数、視聴時間、視聴者属性など）をBigQueryに自動転送するための設定です。
*   **YouTube Content Owner data source**: BigQuery Data Transfer Service のデータソースの一つで、YouTubeのコンテンツ所有者（複数のチャンネルを管理する企業など）全体のアナリティクスデータ（動画のパフォーマンス、収益化データなど）をBigQueryに自動転送するための設定です。
*   **Reach Reports (リーチレポート)**: YouTubeアナリティクスで提供されるレポートの一種で、動画コンテンツや広告がどの程度のユニークな視聴者に届いたか、表示回数がどのくらいあったかなど、「到達度」に関する指標を提供します。これにより、コンテンツの露出や影響範囲を評価するのに役立ちます。
# Title: February 03, 2026 
Link: https://docs.cloud.google.com/release-notes#February_03_2026<br>
# BigQuery
## Announcement
原文: Gemini in BigQuery now processes data in the same jurisdiction (`US` or `EU`) as your BigQuery datasets, or based upon user-specified location settings. For more information, see Where Gemini BigQuery processes your data.

説明：BigQueryのAI機能であるGeminiが、データの処理場所（司法管轄区）をBigQueryデータセットと同じリージョン（`US`または`EU`）で行うようになりました。または、ユーザーが明示的に指定したロケーション設定に基づいて処理されます。この変更により、データ主権やコンプライアンス要件への対応が強化されます。

影響有無：**影響なし（ポジティブな影響の可能性あり）**
この変更は、Geminiによるデータ処理が既存のBigQueryデータセットのロケーションに自動的に準拠するようになるため、既存のデータ主権やコンプライアンスポリシーを維持しやすくなります。明示的にユーザーがロケーション設定を行っていない場合でも、データセットと同じ司法管轄区で処理されるため、意図しないデータ移動は発生しません。コンプライアンス要件が厳しい組織にとっては、歓迎される変更です。

対処方法：**基本的に対処不要**
データ主権やコンプライアンス要件の観点から、Geminiの処理ロケーションがデータセットと同じ司法管轄区にあることが重要である場合、この変更は特に対応を必要としません。
ただし、以下の点を確認することをお勧めします。
1.  **既存のBigQueryデータセットのロケーション確認:** 現在利用しているBigQueryデータセットがどこに存在するかを再確認してください。
2.  **コンプライアンス要件の再確認:** 自社のデータ所在地に関するコンプライアンス（GDPR, CCPAなど）が満たされているか、この変更によってさらに強化されるかを確認してください。
3.  **特定のロケーション要件がある場合:** もしGeminiの処理ロケーションをデータセットのロケーションとは別に、かつ明示的に制御する必要がある場合は、提供されたリンク「[Where Gemini BigQuery processes your data](https://docs.cloud.google.com/bigquery/docs/gemini-locations)」を参照し、ユーザー指定のロケーション設定方法を確認してください。

用語説明：
*   **Gemini in BigQuery:** Google CloudのBigQueryに統合された、Googleの最先端のAIモデルです。データ分析、要約、コード生成、データのパターン認識など、BigQueryのデータを活用した高度なAI機能を提供します。
*   **Jurisdiction (司法管轄区):** 特定の法律や規制が適用される地理的な区域を指します。データ主権（Data Sovereignty）やデータ所在地のコンプライアンス（例: GDPR, CCPA）において非常に重要な概念です。
*   **Data Location / Processing Location (データの所在地 / 処理場所):** データが物理的に保存されている場所、またはデータが計算・分析されるサーバーの地理的な場所を示します。多くの企業や政府機関にとって、データの所在地はセキュリティ、プライバシー、および法的要件を満たす上で重要な考慮事項となります。
# Title: February 02, 2026 
Link: https://docs.cloud.google.com/release-notes#February_02_2026<br>
Google Cloud のリリースノートに基づき、構築済みのサービスへの影響調査結果を報告します。

---

# API Gateway
## Change
原文: `Connect API Gateway to Apigee API hub instances that use VPC Service Controls. API Gateway can now be connected to Apigee API hub instances that use VPC Service Controls.`
説明：
API Gateway が、VPC Service Controls を利用する Apigee API hub インスタンスと接続できるようになりました。これにより、API Gateway と Apigee API hub 間でのデータフローを、VPC Service Controls のサービス境界内で保護することが可能になり、データ漏洩リスクを軽減し、よりセキュアなアーキテクチャを構築する選択肢が追加されました。

影響有無：なし
これは新機能の追加であり、既存の API Gateway や Apigee API hub の構成に自動的に適用される変更ではないため、現在の環境に直接的な影響はありません。既存の接続が中断されたり、動作が変わったりすることはありません。

対処方法：
現在のサービスに影響はないため、直ちに対応する必要はありません。しかし、将来的に API Gateway と Apigee API hub の連携を検討する際、または既存の連携でセキュリティを強化したい場合には、この新機能の利用を検討してください。VPC Service Controls を適用することで、データレジデンシーやデータ保護に関するコンプライアンス要件への対応を強化できます。

用語説明：
*   **API Gateway**: Google Cloud のバックエンドサービス (Cloud Functions, Cloud Run, App Engine, Compute Engine など) に対する API アクセスを統一的に管理・保護するためのフルマネージドサービスです。
*   **Apigee API hub**: Apigee の持つ API 管理機能を活用し、組織内の API を発見、共有、再利用するためのプラットフォームです。API のエコシステムを構築・管理することを目的としています。
*   **VPC Service Controls**: Google Cloud のサービスに対するデータ漏洩リスクを軽減するためのセキュリティ機能です。指定したサービス境界内にリソースを限定し、境界外へのデータ移動を制限することで、機密データを保護します。

---

# Apigee X
## Issue
原文: `Known Issue: 480997525 - Proxy calls fail with The URI contain illegal characters error after Netty upgrade`
説明：
Apigee X において、内部で使用されている Netty というネットワークフレームワークのアップグレード後に、一部のプロキシ呼び出しが「The URI contain illegal characters」（URI に不正な文字が含まれている）というエラーで失敗する既知の問題が報告されています。これは、URI のエンコーディングや特殊文字の処理に関する問題である可能性があります。

影響有無：あり（条件付き）
Apigee X を利用しており、かつ Netty のアップグレード後に、特定の文字（特に日本語などの非 ASCII 文字やエンコードされていない特殊記号など）を含む URI パスやクエリパラメータを使用しているプロキシ呼び出しを行っている場合に、このエラーが発生する可能性があります。
お客様の環境では Google Cloud Composer 2 (Composer version 2.7.1、Airflow version 2.7.3) をご利用とのことですが、Airflow から Apigee X を直接利用している場合は、この問題の影響を受ける可能性があります。Apigee X を利用していない場合は影響ありません。

対処方法：
この問題は既知の不具合として報告されており、Google Cloud による修正パッチのリリースが待たれます。
*   Apigee X を利用している場合は、Apigee X のプロキシ呼び出しで、特に URI に特殊文字や非 ASCII 文字を使用している箇所がないか確認してください。
*   もし問題が発生している場合は、Google Cloud の Apigee サポートドキュメントや「Known Issues」ページ (提供されたリンク) を定期的に確認し、回避策や修正に関する情報を入手してください。
*   緊急を要する場合は、URI 設計を見直し、エラーが発生しないような安全な文字セットで URI を構成することを検討してください。

用語説明：
*   **Apigee X**: Google Cloud 上で提供される、API の設計、公開、セキュリティ、分析、監視を行うためのフルマネージドな API 管理プラットフォームです。
*   **Netty**: Java で書かれた、高性能なネットワークアプリケーション（クライアントおよびサーバー）を開発するための非同期イベント駆動型ネットワークアプリケーションフレームワークです。Apigee の内部コンポーネントとして利用されています。
*   **Proxy calls**: Apigee において、API プロキシを介してクライアントからバックエンドサービスへのリクエスト転送を指します。
*   **URI (Uniform Resource Identifier)**: インターネット上のリソースを一意に識別するための文字列です。URL (Uniform Resource Locator) は URI の一種です。