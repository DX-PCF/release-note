
# Title: September 12, 2025 
Link: https://cloud.google.com/release-notes#September_12_2025<br>
Google Cloudのリリースノートに基づき、各製品の変更点と既存サービスへの影響について調査しました。

---

# Apigee X
## Announcement
原文: On September 12, 2025, we released an updated version of Apigee (1-16-0-apigee-2).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明：Apigee Xの新しいバージョン（1-16-0-apigee-2）が2025年9月12日にリリースされました。このリリースは本日（リリースノート発行日）から段階的にGoogle Cloudの全ゾーンで展開され、完了までに4営業日以上かかる場合があります。お使いのApigeeインスタンスには、このロールアウトが完了するまで新機能や修正が適用されない可能性があります。

影響有無：間接的に影響あり。
既存のApigee Xインスタンスは、今回のリリースで提供される新しいバージョンに自動的にアップデートされる可能性があります。具体的な機能変更や非互換性に関する詳細は発表されていませんが、一般的にパッチバージョンアップは互換性を保つ傾向にあります。
セキュリティ修正（後述）も含まれるため、全体のセキュリティ体制は向上します。

対処方法：特に必要ありませんが、ロールアウト完了後にApigee Xで提供しているAPIの基本的な動作確認を実施することを推奨します。万一、予期せぬ動作変更が確認された場合は、詳細調査が必要です。

## Security
原文:
| Bug ID | Description |
| --- | --- |
| **N/A** | **Security fix for `apigee-runtime`.** |

説明：Apigee Xのコア実行環境である`apigee-runtime`に対するセキュリティ修正が適用されました。具体的なバグIDは公開されていませんが、これによりサービスのセキュリティが強化されます。

影響有無：直接的な影響なし（セキュリティ向上）。
既存のApigee X環境において、セキュリティ脆弱性が修正されるため、ポジティブな影響があります。サービスが中断されたり、設定変更が必要になったりするような直接的な影響はありません。

対処方法：不要です。自動的なバージョンアップによって修正が適用されます。

用語説明：
*   **Apigee X:** Google Cloudが提供するAPI管理プラットフォームの最新バージョン。APIの設計、デプロイ、セキュリティ、分析、モニタリングを行うことができる。
*   **`apigee-runtime`:** Apigee Xにおいて、APIプロキシが実際に動作するランタイム環境。
*   **ロールアウト (Rollout):** ソフトウェアの新しいバージョンや機能を、一度に全体に適用するのではなく、段階的に展開していくプロセス。これにより、問題発生時の影響範囲を限定し、リスクを低減する。

---

# Cloud Load Balancing
## Changed
原文: The global and classic external Application Load Balancers implemented on Google Front-Ends (GFEs) now support HTTP/1.0 explicitly as a protocol during ALPN (Application-Layer Protocol Negotiation) negotiation.

Previously, when the GFEs didn't support HTTP/1.0 explicitly, the GFE would return an `SSL_TLSEXT_ERR_NOACK` response, disable ALPN, and fall back to using HTTP/1 as the default application protocol. After this change, GFEs will instead return `HTTP/1.0`, which provides clients with positive confirmation that their advertised `HTTP/1.0` was accepted.
You are not expected to make any changes with this update. If a TLS handshake with HTTP/1.0 is unsuccessful, please contact support.

You are not expected to make any changes with this update. If a TLS handshake with HTTP/1.0 is unsuccessful, please contact support.
[support](https://cloud.google.com/load-balancing/docs/getting-support)

説明：グローバルおよび従来の外部アプリケーションロードバランサー（Google Front-Ends: GFEsで実装）が、ALPN (Application-Layer Protocol Negotiation) ネゴシエーション中にHTTP/1.0プロトコルを明示的にサポートするようになりました。
以前は、GFEsがHTTP/1.0を明示的にサポートしていなかった場合、`SSL_TLSEXT_ERR_NOACK`エラーを返し、ALPNを無効にしてHTTP/1にフォールバックしていました。この変更により、GFEsは`HTTP/1.0`を返すようになり、クライアントが広告した`HTTP/1.0`が受け入れられたことを確実に確認できるようになります。
このアップデートに伴う変更は不要と明記されており、HTTP/1.0でのTLSハンドシェイクが失敗した場合はサポートへの問い合わせが推奨されています。

影響有無：直接的な影響なし（機能改善）。
既存のCloud Load Balancing設定や、その背後にあるアプリケーション、クライアントに対して、設定変更や動作変更は必要ありません。この変更は、特にHTTP/1.0を使用するクライアントとのALPNネゴシエーションの挙動を改善し、より安定した接続確立を促進するものです。既存のワークロードへの負の影響は想定されていません。

対処方法：不要です。

用語説明：
*   **ALPN (Application-Layer Protocol Negotiation):** TLSハンドシェイク中にクライアントとサーバーがどのアプリケーションプロトコル（例: HTTP/1.1、HTTP/2、HTTP/3）を使用するかをネゴシエートするためのTLS拡張。
*   **Google Front-Ends (GFEs):** Googleのネットワークエッジに配置された分散システムで、ユーザーからのトラフィックを処理し、ロードバランシング、DDoS防御、キャッシュなどの機能を提供する。Google Cloudの外部ロードバランサーの基盤となっている。
*   **HTTP/1.0:** Hypertext Transfer Protocolのバージョン1.0。後のHTTP/1.1やHTTP/2に比べて機能が限定的だが、一部のレガシーなクライアントやシステムでまだ使用されている可能性がある。
*   **`SSL_TLSEXT_ERR_NOACK`:** TLS拡張機能のネゴシエーションにおいて、サーバーがクライアントの要求に応答しなかった（Acknowledgmentがなかった）ことを示すエラー。
# Title: September 11, 2025 
Link: https://cloud.google.com/release-notes#September_11_2025<br>
# Apigee X
## Changed
原文: API hub navigation update
The **API hub** section is now moved to the top level of the Apigee left navigation menu. This change improves discoverability and access to the API hub features.

説明: Apigeeの管理コンソールにおける左側のナビゲーションメニューで、「API hub」セクションが最上位レベルに移動しました。この変更は、APIハブ機能の視認性とアクセス性を向上させることを目的としています。

影響有無: 影響なし
この変更はGoogle Cloudコンソールのユーザーインターフェース (UI) の配置変更のみであり、既存のApigee APIプロキシ、デプロイメント、またはランタイム動作には影響を与えません。管理操作におけるAPIハブへのアクセスパスが変更されるだけです。

対処方法: なし
特別な対応は不要です。Apigeeの管理者は、コンソールのUI変更に慣れる必要があります。

用語説明:
*   **API hub**: Apigeeの機能の一つで、APIカタログの管理や公開、API利用者の発見を支援するポータルです。
*   **ナビゲーションメニュー**: Google Cloudコンソールの左側に表示される、各サービスや機能へのリンクが集約されたメニューです。

---

# Google Kubernetes Engine

## Changed (Extended channel)
原文:
**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

- Version 1.33.4-gke.1036000 is now the default version for cluster creation in the Extended channel.
- The following versions are now available in the Extended channel:
    - 1.28.15-gke.2599000
    - 1.28.15-gke.2630000
    - 1.29.15-gke.1820000
    - 1.29.15-gke.1851000
    - 1.30.14-gke.1108000
    - 1.31.12-gke.1060000
    - 1.32.8-gke.1108000
    - 1.33.4-gke.1134000
- The following versions are no longer available in the Extended channel:
    - 1.28.15-gke.2547000
    - 1.28.15-gke.2610000
    - 1.29.15-gke.1756000
    - 1.29.15-gke.1835000
    - 1.30.14-gke.1036000
    - 1.31.12-gke.1014000
    - 1.32.7-gke.1079000
    - 1.33.3-gke.1136000
- Auto-upgrade targets are now available for the following minor versions:
    - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version 1.28.15-gke.2564000 with this release.
- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
    - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version 1.28.15-gke.2564000 with this release.
    - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version 1.29.15-gke.1773000 with this release.
    - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version 1.30.14-gke.1059000 with this release.
    - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version 1.32.8-gke.1026000 with this release.
    - Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version 1.33.4-gke.1036000 with this release.

説明: GKEのExtendedリリースチャネルにおいて、利用可能なGKEバージョンが更新されました。新規クラスタ作成時のデフォルトバージョンは`1.33.4-gke.1036000`になりました。複数のパッチバージョンが新たに追加され、既存の古いパッチバージョンは利用不可になりました。また、自動アップグレードが有効なクラスタに対して、特定のマイナーバージョン (例: 1.27から1.28) やパッチバージョン (例: 1.28内の最新パッチ) へのアップグレードターゲットが設定されました。

影響有無: 影響あり（間接的）
Google Cloud Composer 2.7.1は内部的にGKEクラスタ（通常はRegularチャネル）を利用しており、現在GKE 1.27.x, 1.28.x, 1.29.x, 1.30.xをサポートしています。Extendedチャネルのクラスタを利用している場合、既存のクラスタが自動アップグレードの対象となる可能性があります。特に、バージョン1.27から1.28へのマイナーバージョンアップグレードや、1.28、1.29、1.30などのパッチバージョンアップグレードは、Composerクラスタに影響を与える可能性があります。これらのアップグレードは通常、互換性を維持するように設計されていますが、ごく稀にAirflow DAGの挙動に影響を与えるケースも報告されています。

対処方法:
1.  **環境の確認**: 運用中のComposer環境がExtendedチャネルを使用しているか、また現在のGKEバージョンを確認してください。
2.  **アップグレード計画の確認**: 自動アップグレードが有効な場合、設定されているメンテナンスウィンドウ内でアップグレードが実行されます。Composer環境のGKEバージョンがアップグレードされる際は、Airflow DAGの動作監視を強化することを推奨します。
3.  **互換性の確認**: 現在使用しているAirflow DAGが、アップグレード後のGKEバージョンで正常に動作するかをテスト環境で検証することが理想的です。Google Cloud Composerの公式ドキュメントで、Composer 2.7.1がサポートするGKEバージョンの詳細を確認してください。

用語説明:
*   **Extended channel (拡張チャネル)**: GKEのリリースチャネルの一つで、Stableチャネルよりも新しいバージョンを比較的長期間利用できるチャネルです。
*   **自動アップグレード (Auto-upgrade)**: GKEクラスタのコントロールプレーンおよびノードが、Googleによって自動的に新しいバージョンに更新される機能です。メンテナンスウィンドウを設定することで、アップグレードのタイミングを制御できます。
*   **パッチバージョン (Patch version)**: ソフトウェアバージョニングにおける3番目の数値（例: v1.28.15の「15」）。バグ修正やセキュリティ修正が主で、通常は下位互換性を持ちます。
*   **マイナーバージョン (Minor version)**: ソフトウェアバージョニングにおける2番目の数値（例: v1.28.15の「28」）。新機能の追加や既存機能の改善が含まれることが多く、稀に非互換の変更が発生する可能性があります。

## Changed (General channel update)
原文:
**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

- Version 1.33.4-gke.1036000 is now the default version for cluster creation.
- The following versions are now available:
    - 1.30.14-gke.1150000
    - 1.31.12-gke.1110000
    - 1.32.8-gke.1170000
    - 1.33.4-gke.1245000
- The following node versions are now available:
    - 1.28.15-gke.2630000
    - 1.29.15-gke.1851000
    - 1.30.14-gke.1150000
    - 1.31.12-gke.1110000
    - 1.32.8-gke.1170000
    - 1.33.4-gke.1245000
- The following versions are no longer available:
    - 1.30.12-gke.1414000
    - 1.31.12-gke.1014000
    - 1.32.7-gke.1016000
    - 1.33.2-gke.1043000
    - 1.33.2-gke.1240000
- Auto-upgrade targets are now available for the following minor versions:
    - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version 1.30.14-gke.1059000 with this release.
- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
    - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version 1.30.14-gke.1059000 with this release.
    - Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version 1.33.4-gke.1036000 with this release.

説明: GKEの特定のチャネルに限定されない一般的なバージョンアップデート情報です（多くの場合、Regularチャネルに該当します）。新規クラスタ作成時のデフォルトバージョンは`1.33.4-gke.1036000`になりました。複数の新しいGKEバージョンが利用可能になり、ノードバージョンも更新されました。いくつかの古いバージョンは利用不可になりました。自動アップグレードが有効なクラスタは、バージョン1.29から1.30へのマイナーアップグレード、および1.30や1.33のパッチアップグレードのターゲットとなります。

影響有無: 影響あり（間接的）
Google Cloud Composer 2.7.1はGKE 1.27.x, 1.28.x, 1.29.x, 1.30.xをサポートしています。このリリースノートでは、バージョン1.29から1.30への自動アップグレードが示されています。これは、Composer環境の基盤となるGKEクラスタが自動アップグレードの対象となる場合に、マイナーバージョンアップグレードが発生する可能性を示唆しています。Composer環境のGKEバージョンがアップグレードされた場合、互換性には通常問題ありませんが、念のためAirflow DAGの動作確認が推奨されます。

対処方法:
1.  **環境の確認**: 運用中のComposer環境の現在のGKEバージョンと、自動アップグレード設定を確認してください。
2.  **アップグレード後の監視**: GKEのマイナーバージョンアップグレードは、新しいAPIや機能の変更が含まれる場合があります。アップグレード後は、Airflow DAGの実行状況とログを注意深く監視し、異常がないか確認してください。
3.  **テストと検証**: 可能な場合は、アップグレード前にテスト環境でAirflow DAGの主要な機能を検証し、アップグレード後に再度検証することが望ましいです。

## Changed (Rapid channel)
原文:
**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

- Version 1.33.4-gke.1172000 is now the default version for cluster creation in the Rapid channel.
- The following versions are now available in the Rapid channel:
    - 1.30.14-gke.1150000
    - 1.31.12-gke.1110000
    - 1.32.8-gke.1170000
    - 1.33.4-gke.1245000
    - 1.34.0-gke.1662000
- The following versions are no longer available in the Rapid channel:
    - 1.30.14-gke.1059000
    - 1.30.14-gke.1108000
    - 1.31.12-gke.1014000
    - 1.32.8-gke.1026000
    - 1.33.4-gke.1036000
    - 1.33.4-gke.1134000
- Auto-upgrade targets are now available for the following minor versions:
    - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version 1.30.14-gke.1130000 with this release.
    - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version 1.31.12-gke.1060000 with this release.
    - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version 1.32.8-gke.1108000 with this release.
    - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version 1.33.4-gke.1172000 with this release.
- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
    - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version 1.30.14-gke.1130000 with this release.
    - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version 1.31.12-gke.1060000 with this release.
    - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version 1.32.8-gke.1108000 with this release.
    - Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version 1.33.4-gke.1172000 with this release.

説明: GKEのRapidリリースチャネルにおいて、利用可能なGKEバージョンが更新されました。新規クラスタ作成時のデフォルトバージョンは`1.33.4-gke.1172000`になりました。注目すべきは、GKE 1.34.0が新たに利用可能バージョンとして追加された点です。複数のパッチバージョンが追加/削除され、自動アップグレードが有効なクラスタに対しては、1.29から1.30、1.30から1.31、1.31から1.32、1.32から1.33へのマイナーバージョンアップグレード、および各マイナーバージョンのパッチアップグレードがターゲットとして設定されました。

影響有無: 影響あり（間接的、限定的）
Google Cloud Composer 2.7.1はGKE 1.27.x, 1.28.x, 1.29.x, 1.30.xをサポートしており、GKE 1.34.xは現時点ではサポート対象外です。通常、Composer環境はRapidチャネルを使用しないため、直接的な影響は限定的です。ただし、もしRapidチャネルを使用しているComposer環境が存在する場合、自動アップグレードによってGKE 1.30, 1.31, 1.32, 1.33へのマイナーバージョンアップグレードが発生し、Composerのサポート範囲を超える可能性があります。これにより、Composer環境が不安定になるリスクがあります。

対処方法:
1.  **環境の確認**: 運用中のComposer環境がRapidチャネルを使用している場合は、直ちにチャネルの見直しを検討し、RegularまたはStableチャネルへの移行を計画してください。
2.  **サポートバージョンの確認**: Composer環境のGKEバージョンが自動アップグレードによりサポート対象外のGKEバージョンに到達しないよう、常にGoogle Cloud Composerの公式ドキュメントでサポートされているGKEバージョンのリストを確認してください。
3.  **非互換性リスクの評価**: Rapidチャネルは最新機能が早く提供される反面、変更が頻繁であり、非互換性が発生するリスクも高いため、Composerのような管理サービスでの利用は非推奨です。

用語説明:
*   **Rapid channel (ラピッドチャネル)**: GKEのリリースチャネルの一つで、最も早く最新のKubernetesバージョンが提供されるチャネルです。新機能を早期に試すためのものですが、頻繁な変更があるため本番環境での利用は慎重に検討する必要があります。

## Changed (Regular channel)
原文:
**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

- Version 1.33.4-gke.1036000 is now the default version for cluster creation in the Regular channel.
- The following versions are now available in the Regular channel:
    - 1.30.14-gke.1108000
    - 1.31.12-gke.1060000
    - 1.32.8-gke.1108000
    - 1.33.4-gke.1134000
- The following versions are no longer available in the Regular channel:
    - 1.30.14-gke.1036000
    - 1.31.12-gke.1014000
    - 1.32.7-gke.1079000
    - 1.33.3-gke.1136000
- Auto-upgrade targets are now available for the following minor versions:
    - Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version 1.30.14-gke.1059000 with this release.
    - Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version 1.32.8-gke.1026000 with this release.
    - Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version 1.33.4-gke.1036000 with this release.
- The following patch-only version auto-upgrade targets are now available for clusters with maintenance exclusions or other factors preventing minor version upgrades:
    - Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version 1.30.14-gke.1059000 with this release.
    - Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version 1.32.8-gke.1026000 with this release.
    - Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version 1.33.4-gke.1036000 with this release.

説明: GKEのRegularリリースチャネルにおいて、利用可能なGKEバージョンが更新されました。新規クラスタ作成時のデフォルトバージョンは`1.33.4-gke.1036000`になりました。複数のパッチバージョンが新たに追加され、既存の古いパッチバージョンは利用不可になりました。自動アップグレードが有効なクラスタに対して、特定のマイナーバージョン (例: 1.29から1.30、1.31から1.32、1.32から1.33) やパッチバージョン (例: 1.30、1.32、1.33内の最新パッチ) へのアップグレードターゲットが設定されました。

影響有無: 影響あり（間接的、中程度）
Google Cloud Composer 2.7.1はGKE 1.27.x, 1.28.x, 1.29.x, 1.30.xをサポートしており、通常Regularチャネルを使用します。このリリースノートでは、バージョン1.29から1.30へのマイナーアップグレードターゲットが示されており、これはComposer 2.7.1のサポート範囲内です。しかし、さらに先のバージョン (1.31から1.32, 1.32から1.33) へのマイナーアップグレードターゲットも示されています。Composer環境のGKEバージョンがComposer 2.7.1のサポート範囲を超えるGKEバージョン（例: GKE 1.31以降）に自動アップグレードされる場合、潜在的な互換性問題が発生するリスクがあります。

対処方法:
1.  **サポートバージョンの継続的な確認**: Google Cloud Composerの公式ド