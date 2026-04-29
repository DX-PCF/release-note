
# Title: April 28, 2026 
Link: https://docs.cloud.google.com/release-notes#April_28_2026<br>
# AlloyDB for PostgreSQL
## Change
原文: When the initial user or password is unspecified during cluster creation, a locked `postgres` role with `null` password is created.

[`postgres` role](https://docs.cloud.com/alloydb/docs/database-users/overview#postgres-user)

説明：
AlloyDB for PostgreSQLのクラスター作成時における、デフォルトの`postgres`ロールの作成挙動に関する変更です。これまでは、クラスター作成時に初期ユーザーやパスワードが明示的に指定されなかった場合の`postgres`ロールの具体的な状態が明確ではありませんでした。この変更により、もし初期ユーザーやパスワードを指定せずにクラスターを作成した場合、自動的に作成される`postgres`ロールは「ロックされた状態」となり、かつ「パスワードがnull」として設定されるようになりました。

影響有無：
*   **既存のAlloyDBクラスターへの影響はありません。** この変更はクラスターの「作成時」の挙動にのみ適用されます。
*   **新規のAlloyDBクラスター作成時に影響があります。**
    *   もし、新規クラスター作成時に、初期ユーザー名とパスワードを明示的に指定しない場合、自動的に作成される`postgres`ロールはロックされた状態（ログイン不可）となり、パスワードも設定されません。
    *   これは、意図せずデフォルトのスーパーユーザーロールがログイン可能な状態で作成されることを防ぎ、セキュリティを強化する変更と見なせます。

対処方法：
*   **推奨される対応:** 新規にAlloyDBクラスターを作成する際は、セキュリティのベストプラクティスとして、初期ユーザー（例: `admin`）と強力なパスワードを常に明示的に指定することを強く推奨します。これにより、初期ユーザーとパスワードが設定され、`postgres`ロールがロックされた状態であっても問題なく運用を開始できます。
*   もし、何らかの理由で初期ユーザーやパスワードを指定せずクラスターを作成し、後から`postgres`ロールを使用したい場合は、クラスター作成後に別途パスワードを設定し、ロールのロックを解除する操作が必要になります。しかし、通常は業務アプリケーション用に別の権限を付与されたユーザーを作成し、`postgres`ロールは緊急時や管理作業にのみ限定的に利用するのが一般的です。

用語説明：
*   **`AlloyDB for PostgreSQL`**: Google Cloudが提供するフルマネージドなPostgreSQL互換のデータベースサービスです。高性能と高可用性を特徴としています。
*   **`postgres` role**: PostgreSQLデータベースにおいて、デフォルトで作成される最も上位の権限を持つスーパーユーザーロール（データベースユーザー）です。すべてのデータベース操作に対する権限を持ちます。
*   **`locked role`**: データベースのロール（ユーザー）がロックされた状態を指します。この状態のロールは、パスワードが正しくてもログインすることができません。セキュリティ上の理由や、一時的なアクセス制限のために利用されます。
*   **`null password`**: パスワードが設定されていない、または明示的にnullとして扱われる状態を指します。ただし、このリリースノートの文脈では、ロール自体がロックされているため、パスワードの有無にかかわらずログインはできません。
# Title: April 27, 2026 
Link: https://docs.cloud.google.com/release-notes#April_27_2026<br>
## API Gateway
### Change
原文: New validations on paths in API configurations. API Gateway now enforces stricter syntax validations on templated paths when you create new API configurations and gateways. See path templating syntax rules and limits for more information.

説明:
API Gateway の API 設定およびゲートウェイ作成時において、テンプレート化されたパスの構文検証がより厳格になりました。これにより、新しいAPI設定やゲートウェイを作成する際に、パスの記述が指定された構文ルールと制限に厳密に準拠している必要があります。

影響有無:
*   **影響あり**: 新規でAPI設定やゲートウェイを作成する際、既存のパス定義が新しい厳格なバリデーションルールに準拠していない場合、エラーが発生し作成に失敗する可能性があります。特に、これまで許容されていたが厳密なルールからは外れていたようなパス定義を使用している場合に影響を受けます。
*   **影響なし**: 既にデプロイ済みのAPI設定やゲートウェイの動作には直接的な影響はありません。ただし、それらを更新・再デプロイする際には、新しいバリデーションが適用される可能性があるため注意が必要です。

対処方法:
新規API設定やゲートウェイをデプロイする前に、既存のパス定義が[path templating syntax rules](https://docs.cloud.google.com/api-gateway/docs/path-templating#syntax_rules)および[limits](https://docs.cloud.google.com/api-gateway/docs/path-templating#limits)に準拠しているか確認してください。バリデーションエラーが発生した場合は、ドキュメントを参照してパスの記述を修正してください。

用語説明:
*   **API Gateway**: フルマネージドなサービスで、REST APIを公開し、バックエンドサービス（Cloud Functions、Cloud Run、App Engineなど）へのアクセスを管理します。
*   **テンプレート化されたパス (Templated paths)**: APIのパス内で、可変部分をプレースホルダーとして定義する記法です。例えば、`/users/{userId}/posts/{postId}` のように記述し、複数のリソースに一致する単一のパス定義を可能にします。
*   **構文検証 (Syntax validations)**: コードや設定ファイルの記述が、定められた文法規則に則っているかをチェックするプロセスです。

---

## Cloud Service Mesh
### Announcement
原文: Managed Cloud Service Mesh using the `TRAFFIC_DIRECTOR` implementation in the regular channel now supports a limited implementation of the `EnvoyFilter` API. To learn about the supported fields, extensions, and how to use `EnvoyFilter` for features like local rate limiting see Data plane extensibility with `EnvoyFilter`. To troubleshoot any issue while configuring, see Resolving data plane extensibility issues.

説明:
Google Cloud のマネージドサービスメッシュ（Traffic Director を利用）が、`EnvoyFilter` API の一部機能をサポートするようになりました。これにより、サービスメッシュのデータプレーンであるEnvoyプロキシの動作を、より低レベルで細かくカスタマイズできるようになります。ローカルレートリミットなどの機能への応用が可能です。サポートされるフィールドや拡張機能、具体的な使用方法については、関連ドキュメントを参照してください。

影響有無:
*   **影響なし**: これは新機能の追加であり、既存のCloud Service Meshの構成や動作に自動的に変更が適用されることはありません。既存のサービスには影響を与えません。
*   **潜在的な影響**: `EnvoyFilter`を利用してカスタムな動作を導入する場合、設定ミスなどにより意図しないトラフィックルーティングやポリシー適用が発生する可能性がありますが、これは利用者が能動的に設定した場合に限られます。

対処方法:
`EnvoyFilter`機能を利用したい場合は、[Data plane extensibility with `EnvoyFilter`](https://docs.cloud.google.com/service-mesh/docs/data-plane-extensibility)ドキュメントを熟読し、サポートされるフィールドや制限事項を理解した上で導入を検討してください。導入後は、十分なテストを実施し、予期せぬ動作がないか確認することが重要です。設定に関する問題が発生した場合は、[Resolving data plane extensibility issues](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-data-plane-extensibility)を参照してトラブルシューティングを行ってください。

用語説明:
*   **Cloud Service Mesh**: Google Cloud のフルマネージドなサービスメッシュソリューションです。サービス間の通信を制御、可視化、保護する機能を提供し、Traffic Director をコントロールプレーンとして利用します。
*   **Traffic Director**: Google Cloud のマネージドなサービスメッシュコントロールプレーンです。Envoy プロキシなどのサイドカーを構成し、トラフィック管理、ロードバランシング、ヘルスチェックなどを提供します。
*   **Envoy プロキシ**: クラウドネイティブなアプリケーション向けに設計された高性能なオープンソースのL7プロキシです。サービスメッシュのデータプレーンとして、アプリケーションのサイドカーとして広く利用されます。
*   **EnvoyFilter API**: Istio や Service Mesh で使用されるカスタムリソース定義 (CRD) で、Envoy プロキシの動作を低レベルでカスタマイズするための柔軟なメカニズムを提供します。フィルタチェーンの変更、ルート設定の調整、メトリクスの追加など、高度なユースケースに対応できます。
*   **データプレーン (Data plane)**: サービスメッシュにおいて、実際にネットワークトラフィックが流れる部分を指します。通常、アプリケーションのサイドカーとしてデプロイされたEnvoyプロキシがデータプレーンを構成します。
*   **コントロールプレーン (Control plane)**: サービスメッシュにおいて、データプレーンのプロキシ（例: Envoy）を設定・管理する部分です。Traffic Director や Istio のコンポーネントがこれにあたります。