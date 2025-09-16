
# Title: September 12, 2025 
Link: https://cloud.google.com/release-notes#September_12_2025<br>
承知いたしました。Google Cloudのリリースノートを元に、構築済みのサービスへの影響有無を調査し、ご指定の形式で回答します。

---

# Apigee X
## Announcement
原文: On September 12, 2025, we released an updated version of Apigee (1-16-0-apigee-2).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明：Apigee Xの新しいバージョン（1-16-0-apigee-2）がリリースされました。このリリースは本日よりGoogle Cloudの全ゾーンで順次ロールアウトが開始されており、完了までに4営業日以上かかる場合があります。このロールアウトが完了するまで、お客様のApigeeインスタンスでは新しい機能や修正が利用できない可能性があります。リリースノートの記載日（2025年9月12日）は将来の日付ですが、これはリリースノートの記載上のタイムスタンプである可能性が高く、実際のロールアウトはリリースノートが公開された日から開始されています。

影響有無：
*   **影響あり**: Apigee XはGoogle Cloudのマネージドサービスであるため、バージョンアップは自動的に適用されます。新しいバージョンが適用されることで、バグ修正や機能改善が提供されますが、稀に予期せぬ挙動変更が発生する可能性も考慮する必要があります。
*   **影響なし**: 既存のAPIトラフィックや設定に対して、即座に破壊的な変更が導入されるものではありません。

対処方法：
*   **監視**: ロールアウト期間中および完了後に、Apigee XでデプロイしているAPIプロキシやサービスに異常がないか、モニタリングを継続してください。
*   **リリースノート確認**: 今後のApigee Xのリリースノートで、このバージョンに含まれる具体的な変更点（新機能、バグ修正、既知の問題など）が詳細に発表される可能性があります。これを確認し、既存の構成への影響や活用できる新機能がないか評価することを推奨します。

用語説明：
*   **Rollout**: ソフトウェアの新しいバージョンや機能が、システム全体に段階的に展開され、適用されていくプロセス。ユーザーへの影響を最小限に抑えるために段階的に行われることが多いです。
*   **Google Cloud zones**: Google Cloudリソースがデプロイされる、物理的に独立した地理的エリア。可用性ゾーンとも呼ばれ、同じリージョン内のゾーン間で障害が隔離されるように設計されています。

## Security
原文:
| Bug ID | Description |
| --- | --- |
| **N/A** | **Security fix for `apigee-runtime`.** |

説明：Apigeeのコアランタイムコンポーネントである`apigee-runtime`に対してセキュリティ修正が適用されました。特定のバグIDは公開されていませんが、これによりApigee Xのセキュリティ体制が強化されます。

影響有無：
*   **影響あり（ポジティブ）**: セキュリティ修正が含まれるため、Apigee Xサービスのセキュリティが向上します。これはお客様のAPIゲートウェイの保護に寄与するポジティブな影響です。

対処方法：
*   **特になし**: マネージドサービスであるため、セキュリティ修正は自動的に適用されます。ユーザー側での具体的な操作は不要です。

用語説明：
*   **`apigee-runtime`**: Apigee API Gateway の中核をなすランタイムコンポーネント。APIプロキシのデプロイ、トラフィックのルーティング、ポリシーの実行、分析データの収集など、API処理の主要な機能を担当します。

---

# Cloud Load Balancing
## Changed
原文: The global and classic external Application Load Balancers implemented on Google Front-Ends (GFEs) now support HTTP/1.0 explicitly as a protocol during ALPN (Application-Layer Protocol Negotiation) negotiation.

Previously, when the GFEs didn't support HTTP/1.0 explicitly, the GFE would return an `SSL_TLSEXT_ERR_NOACK` response, disable ALPN, and fall back to using HTTP/1 (which includes HTTP/1.0 and HTTP/1.1) as the default application protocol. After this change, GFEs will instead return `HTTP/1.0`, which provides clients with positive confirmation that their advertised `HTTP/1.0` was accepted.
You are not expected to make any changes with this update. If a TLS handshake with HTTP/1.0 is unsuccessful, please contact support.

説明：Google Front-Ends (GFEs) で動作するグローバルおよび従来の外部Application Load Balancerにおいて、ALPN（Application-Layer Protocol Negotiation）ネゴシエーション時にHTTP/1.0プロトコルが明示的にサポートされるようになりました。
これまでは、GFEがHTTP/1.0を明示的にサポートしていない場合、ALPNネゴシエーションで`SSL_TLSEXT_ERR_NOACK`を返し、ALPNを無効化し、HTTP/1 (HTTP/1.0およびHTTP/1.1を含む) をデフォルトのアプリケーションプロトコルとしてフォールバックしていました。今回の変更により、GFEはクライアントが要求したHTTP/1.0を受け入れたことを示すために明示的に`HTTP/1.0`を返すようになり、クライアント側でのプロトコル合意の確認がより明確になります。

影響有無：
*   **影響なし**: リリースノートに「You are not expected to make any changes with this update. (このアップデートで変更を加えることは想定されていません。)」と明記されているため、既存のロードバランサ設定やアプリケーションに直接的な変更作業は不要です。
*   **影響あり（ポジティブ）**: HTTP/1.0を使用するクライアントが存在する場合、ALPNネゴシエーション時の挙動がより明確になり、プロトコル合意の確実性が向上します。これにより、問題発生時のトラブルシューティングが容易になる可能性があります。

対処方法：
*   **特になし**: この変更によるお客様側での設定変更は想定されていません。
*   **緊急時の対応**: もしこの変更後にHTTP/1.0でのTLSハンドシェイクが失敗するなどの問題が発生した場合は、Google Cloudサポートに連絡してください。

用語説明：
*   **Application Load Balancer**: HTTP(S)トラフィックに特化したレイヤー7のロードバランサーで、URLパス、ヘッダー、Cookieなどのアプリケーション層の情報に基づいてトラフィックをルーティングします。
*   **Google Front-Ends (GFEs)**: Googleのグローバルネットワークエッジに配置された分散インフラストラクチャ。ロードバランシング、DDoS対策、TLS終端、コンテンツキャッシュなどの機能を提供し、Google Cloudサービスのパフォーマンスとセキュリティを支えています。
*   **ALPN (Application-Layer Protocol Negotiation)**: TLSハンドシェイク中にクライアントとサーバーが、どのアプリケーションプロトコル（例: HTTP/1.1, HTTP/2, HTTP/3）を使用するかを合意するためのプロトコル拡張。これにより、1回のラウンドトリップでプロトコルの選択が完了し、接続確立の効率が向上します。
*   **HTTP/1.0**: Hypertext Transfer Protocolの初期バージョンの一つ。現在のWebではHTTP/1.1やHTTP/2が主流ですが、特定の古いクライアントや特殊な環境ではまだ使用されることがあります。

---