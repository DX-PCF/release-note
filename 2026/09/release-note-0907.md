
# Title: September 04, 2026 
Link: https://docs.cloud.google.com/release-notes#September_04_2026<br>
# Cloud Billing
## Change
原文: **Introducing the Incentives page, for tracking spend-based milestone credits, RaMP, and other conditional incentives**

If you have a custom pricing contract, you might be enrolled in conditional incentives, where you earn credits or discounts for spending specific amounts on Google Cloud.

The **Incentives page** replaces the *Spend-based Milestones tab* that was located in the *Credits* page. The Incentives page provides a consolidated and enhanced experience for tracking your progress towards conditional incentives, including spend-based milestone credits and Rapid Migration & Modernization Program (RaMP) credits and discounts.

[**Incentives page**](https://docs.cloud.google.com/billing/docs/how-to/incentives-program-tracker)
[*Spend-based Milestones tab*](https://docs.cloud.google.com/billing/docs/release-notes#July_22_2024)
Learn more about tracking conditional incentives.

[tracking conditional incentives](https://docs.cloud.google.com/billing/docs/how-to/incentives-program-tracker)

説明：
Google Cloud Billingにおいて、条件付きインセンティブ（特定の支出額に応じてクレジットや割引が付与されるプログラム）の追跡を目的とした新しいインターフェース「Incentives page」が導入されました。この新ページは、これまでの「Credits」ページ内にあった「Spend-based Milestones tab」を置き換えるものです。これにより、支出ベースのマイルストーンクレジットやRapid Migration & Modernization Program (RaMP) クレジットなど、様々な条件付きインセンティブの進捗状況を統合的かつ強化された形式で確認できるようになります。主にカスタム価格契約を結んでいるユーザーが対象です。

影響有無：
**影響なし**
この変更は、Google Cloud ConsoleのUI/UXの改善であり、請求情報の表示方法に関するものです。基盤となる課金ロジック、リソースの利用料金、または既存のアプリケーションやインフラストラクチャの動作に直接的な影響はありません。カスタム価格契約を締結している組織の請求管理担当者や財務担当者がインセンティブの進捗状況を確認する際の利便性が向上するのみです。

対処方法：
システム的な対処は不要です。
カスタム価格契約を結んでいる組織では、経理や財務、あるいはGoogle Cloudの支出を管理している担当者に対し、インセンティブの進捗確認インターフェースが変更された旨を周知することを推奨します。

用語説明：
*   **Incentives page (インセンティブページ):** Google Cloudの請求アカウントにおいて、支出目標の達成に応じて付与されるクレジットや割引（インセンティブ）の進捗状況を統合的に確認できる新しいウェブページ。
*   **Spend-based milestone credits (支出ベースマイルストーンクレジット):** 事前に合意された支出額や利用量といった特定の目標（マイルストーン）を達成した際に、Google Cloudの利用料金に適用されるクレジット。通常、大規模なカスタム価格契約の一環として提供されます。
*   **Rapid Migration & Modernization Program (RaMP) (ラピッドマイグレーション＆モダナイゼーションプログラム):** 顧客が既存のワークロードをGoogle Cloudへ迅速に移行し、モダナイズすることを支援するためにGoogleが提供するプログラム。このプログラムには、移行を促進するためのクレジットや割引が含まれる場合があります。
*   **Custom pricing contract (カスタム価格契約):** Google Cloudの標準的な従量課金制とは異なり、大量利用や長期契約などの特定の条件に基づいて、個別に交渉された料金や割引が適用される契約。通常、エンタープライズ顧客向けに提供されます。
# Title: September 03, 2026 
Link: https://docs.cloud.google.com/release-notes#September_03_2026<br>
# API Gateway
## Change
原文: New model routing gateways might use a gateway.dev default hostname
If you create a gateway that uses model routing on or after September 3, 2026, it might receive a `gateway.dev` default hostname instead of a `run.app` one, in the form `https://GATEWAY_ID-PROJECT_NUMBER.REGION.gateway.dev` — for example, `https://my-gateway-123456789012.us-central1.gateway.dev`. This is a second `gateway.dev` format; other gateways keep the existing one.
To get a gateway's URL, read its `defaultHostname` property.
For more information, see Deploy an API to a gateway.
[Deploy an API to a gateway](https://docs.cloud.google.com/api-gateway/docs/deploying-api)

説明：
2026年9月3日以降に、モデルルーティング（Model Routing）を使用するAPI Gatewayを新規作成する場合、デフォルトのホスト名が従来の`run.app`形式 (`GATEWAY_ID-PROJECT_NUMBER.REGION.run.app`) ではなく、新しい`gateway.dev`形式 (`https://GATEWAY_ID-PROJECT_NUMBER.REGION.gateway.dev`) になる可能性があるというアナウンスです。
これは既存の`gateway.dev`形式 (`GATEWAY_ID.REGION.gateway.dev`) とは異なる、新しい形式の導入となります。
既存のAPI Gatewayのホスト名には影響がなく、変更はありません。
GatewayのURLは、その`defaultHostname`プロパティから取得できることが再度強調されています。

影響有無：
**影響なし（現時点での直接的な影響はなし）**
現在稼働中のAPI Gatewayやシステムには直接的な影響はありません。この変更は2026年9月3日以降に「新規作成される」モデルルーティングを使用するAPI Gatewayにのみ適用される可能性があるためです。
ただし、将来的にAPI Gatewayを新規作成し、その際にモデルルーティングを使用する場合、ホスト名の形式が変わる可能性があることに留意が必要です。もし現在、API GatewayのURLをハードコードしている場合は、将来的な新規作成時に新しいホスト名形式を認識する必要があります。

対処方法：
現時点での緊急対応は不要です。
将来、2026年9月3日以降にモデルルーティングを使用するAPI Gatewayを新規作成する際には、このホスト名変更の可能性を考慮に入れてください。
API GatewayのURLを取得する際は、ベストプラクティスとして、`defaultHostname`プロパティから動的に取得することをお勧めします。これにより、ホスト名形式の変更に依存しない柔軟な構成が可能です。

用語説明：
*   **API Gateway**: Google Cloudが提供するマネージドサービスで、APIの作成、デプロイ、セキュリティ保護、監視、バージョン管理などを一元的に行います。
*   **モデルルーティング (Model Routing)**: API Gatewayのルーティング方式の一つで、OpenAPI Specification（OAS）で定義されたパスやHTTPメソッドに基づいて、受信したリクエストを特定のバックエンドサービスにルーティングします。
*   **`defaultHostname`**: API Gatewayがデプロイされた際に自動的に割り当てられるデフォルトのホスト名です。API Gatewayのリソースのプロパティとして提供され、API GatewayのURLを取得するために使用されます。
*   **OpenAPI Specification (OAS)**: APIの記述形式の標準であり、RESTful APIを機械可読な形で記述するために使用されます。API Gatewayでは、この仕様に基づいてAPIの定義やルーティング設定を行います。