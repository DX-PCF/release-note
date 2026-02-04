
# Title: February 03, 2026 
Link: https://docs.cloud.google.com/release-notes#February_03_2026<br>
# BigQuery
## Announcement
原文: Gemini in BigQuery now processes data in the same jurisdiction (`US` or `EU`) as your BigQuery datasets, or based upon user-specified location settings. For more information, see Where Gemini BigQuery processes your data.

説明：
BigQuery に統合されているAI機能である Gemini が、データ処理を行う際のロケーションに関する挙動を変更しました。今回の変更により、Gemini は BigQuery データセットと同じ司法管轄区域（米国またはEU）内でデータを処理するようになります。また、ユーザーが明示的に指定したロケーション設定に基づいて処理を行うことも可能です。これにより、データ主権およびデータレジデンシーに関するコンプライアンス要件への対応が強化されます。詳細については、公式ドキュメント「Where Gemini BigQuery processes your data」を参照してください。

影響有無：
**影響なし（ポジティブな変更）**

理由：
この変更は、BigQuery の Gemini 機能がデータを処理する際のロケーションに関する透明性とコンプライアンスを向上させるものです。既存のデータセットのロケーション設定に連動するか、ユーザー指定のロケーション設定に従うため、意図しない地理的区域でデータが処理されるリスクが低減されます。これは、特にデータ主権やデータレジデンシーに厳格な要件を持つ組織にとって、コンプライアンス順守を容易にするポジティブな改善であり、既存のワークロードに直接的な非互換性やパフォーマンスへの悪影響はありません。

対処方法：
特別な対処は不要です。しかし、貴社のデータガバナンスポリシーや特定の規制（例：GDPR, FedRAMPなど）においてデータレジデンシーに厳格な要件がある場合は、BigQuery データセットのロケーション設定および Gemini の `user-specified location settings` が、これらの要件を満たしているか改めて確認し、必要に応じて設定を見直すことを推奨します。

用語説明：
*   **Gemini in BigQuery**: Google Cloud のビッグデータウェアハウスサービスである BigQuery に統合された、Google の基盤AIモデル（Gemini）。SQLクエリの生成支援、データの分析と洞察の提供、効率的なデータ変換など、BigQuery 環境での生産性向上を目的とした機能です。
*   **Jurisdiction (司法管轄区域)**: データの保管、処理、および利用が法的・規制的に管轄される地理的区域を指します。データプライバシーやデータ主権の観点から重要視されます。
*   **Data Residency (データレジデンシー)**: データが物理的に保管され、処理される地理的な場所に関する要件を指します。多くの国や地域では、特定の種類のデータ（例：個人情報）を国内に留めておくことを義務付ける法律や規制が存在します。
*   **User-specified location settings**: ユーザーが明示的に指定する、Google Cloud サービスがデータを保管・処理する地理的な場所の設定を指します。例えば、BigQuery データセットを作成する際に指定するリージョンやマルチリージョンがこれに該当します。
# Title: February 02, 2026 
Link: https://docs.cloud.google.com/release-notes#February_02_2026<br>
Google Cloud インフラエンジニアとして、お問い合わせいただいたリリースノートについて、既存サービスへの影響有無を調査し、以下の通りご回答いたします。

---

# API Gateway

## Change

原文: `API Gateway can now be connected to Apigee API hub instances that use VPC Service Controls.`

[connected to Apigee API hub](https://docs.cloud.google.com/api-gateway/docs/api-hub-connect)
[VPC Service Controls](https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc)

説明：
API Gatewayが、VPC Service Controlsが有効化されたApigee API hubインスタンスと接続可能になったという機能拡張アナウンスです。これにより、データ漏洩防止のためのセキュリティ境界（VPC Service Controls）内で、API GatewayからApigee API hubへのセキュアな接続が実現可能になります。

影響有無：
影響はありません。
本変更は新機能の追加であり、既存のAPI Gatewayの動作や設定に直接的な影響を与えるものではありません。現在、VPC Service Controls環境でAPI GatewayとApigee API hubの連携を行っていない場合は、特に影響は発生しません。
将来的にVPC Service Controlsの導入や、API GatewayとApigee API hubの連携を検討する際に、この新機能が利用可能であるというメリットとして認識しておくべき変更です。

対処方法：
既存システムへの影響はないため、即座の対処は不要です。
今後、VPC Service Controls環境下でのAPI GatewayとApigee API hubの連携を計画する際には、公式ドキュメントを参照の上、本機能の活用を検討してください。

用語説明：
*   **API Gateway**: Google Cloud 上で構築されたAPIに対するアクセスを管理、セキュリティ保護、監視するためのフルマネージドサービスです。
*   **Apigee API hub**: APIのライフサイクル全体を管理するためのプラットフォームで、APIの発見、共有、再利用、統制を促進します。企業内のAPI資産のカタログ化や共同作業を支援します。
*   **VPC Service Controls (Virtual Private Cloud Service Controls)**: Google Cloudリソースのデータ漏洩リスクを軽減するために、サービス境界を作成し、その境界を越えたデータ転送を制限するセキュリティ機能です。これにより、機密データの流出を防ぎます。

---

# Apigee X

## Issue

原文: `Known Issue: 480997525 - Proxy calls fail with The URI contain illegal characters error after Netty upgrade`

[480997525 - Proxy calls fail with `The URI contain illegal characters` error after Netty upgrade](https://docs.cloud.google.com/apigee/docs/release/known-issues#480997525)

説明：
Apigee Xの既知の問題に関するアナウンスです。
Apigee内部で使用されているNettyコンポーネントのアップグレード後、特定のURI（Uniform Resource Identifier）が不正な文字を含んでいると判断され、「The URI contain illegal characters」というエラーメッセージとともにプロキシ呼び出しが失敗する可能性があるという内容です。

影響有無：
Apigee Xをご利用の場合、影響を受ける可能性があります。
これは「既知の不具合」であり、もし現在、Apigee Xを介したAPIプロキシ呼び出しで「The URI contain illegal characters」エラーが発生している場合、本件が原因である可能性が高いです。特に、URIに特殊文字や非ASCII文字が含まれる場合に発生しやすいと考えられます。

対処方法：
このリリースノート自体には解決策の記載がないため、速やかにリンク先の「Known Issues」ドキュメント（[480997525 - Proxy calls fail with `The URI contain illegal characters` error after Netty upgrade](https://docs.cloud.google.com/apigee/docs/release/known-issues#480997525)）を参照し、詳細な情報や回避策、または修正の状況を確認してください。
現時点でエラーが発生していない場合でも、将来的な問題に備え、当該ドキュメントを定期的に確認することをお勧めします。

用語説明：
*   **Apigee X**: Google Cloudが提供するフルマネージドなAPI管理プラットフォームです。APIの設計、セキュリティ保護、公開、分析、監視といったAPIライフサイクル管理の包括的な機能を提供します。
*   **Proxy calls (プロキシ呼び出し)**: クライアントからのAPIリクエストが、Apigee APIプロキシを介してバックエンドサービスに転送される一連の処理を指します。Apigeeがクライアントとバックエンドサービス間の仲介役となります。
*   **Netty**: Javaで書かれた高性能な非同期イベント駆動型ネットワークアプリケーションフレームワークです。Apigeeの内部でネットワーク通信を処理するコンポーネントとして利用されている可能性があります。
*   **URI (Uniform Resource Identifier)**: インターネット上のリソースを一意に識別するための文字列です。URL（Uniform Resource Locator）はURIの一種であり、リソースの場所を示します。特定の文字がURIの構文規則に違反している場合に「illegal characters」エラーが発生します。